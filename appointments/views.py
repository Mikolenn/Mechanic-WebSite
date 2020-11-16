from django.shortcuts import render
from django.http import Http404
from .models import Car
from .forms import CarForm, CarStaffForm
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User


# Función staff. Permite mostrar las citas prendientes de los usuarios
# de tipo administrativo. Recibe el identificador único, del objeto con url
# seleccionado y, lo utiliza para desplegar los datos de ese objeto específico

@staff_member_required
def staff(request, pk=None):

    if pk is not None:

        try:
            car = Car.objects.get(pk=pk)

        except Car.DoesNotExist:

            # Caso en el que el identificador ingresado  no corresponde
            # con ninguna cita registrada
            raise Http404('El auto con identificador {} no existe'.format(pk))

        return render(
            request,
            'staff.html',
            {
                'pk': car.pk,
                'user_first_name': car.user.first_name,
                'user_last_name': car.user.last_name,
                'brand': car.brand,
                'car_model': car.car_model,
                'year': car.year,
                'transmision': car.transmission,
                'schedule': car.schedule,
                'date': car.date,
                'provider': car.provider
            }
        )

    else:

        car_dict = {}

        for car in Car.objects.all():
            if request.user == car.provider:
                car_dict[car.pk] = {
                    'pk': car.pk,
                    'brand': car.brand,
                    'car_model': car.car_model,
                    'year': car.year
                }

        return render(
            request,
            'staff.html',
            {
                'car_dict': car_dict
            }
        )


# Función base. Permite realizar la renderización del template base, el cual
# contiene la configuración base, a partir de la cual se construyen los
# restantes templates

def base(request):
    return render(request, 'base.html', {})


# Función delete. Permite eliminar objetos tipo car. Recibe el identificador
# único del objeto a eliminar

def delete(response, pk=None):

    if pk is not None:

        instance = get_object_or_404(Car, pk=pk)
        instance.delete()
        return redirect('view')

    else:
        return redirect('view')


# Función create. Permite la creación y modificación de los objetos de tipo
# car. Recibe el identificador único del objeto, por medio del url
# seleccionado y, lo emplea para desplegar el formulario del mismo para su
# modificación. Si no recibe el identificador, muestra el formulario estándar
# para crear el nuevo objeto

def create(response, pk=None):

    # Caso en el cual se selecciona el url de modificación de cita
    if pk is not None:
        instance = get_object_or_404(Car, pk=pk)
        form = CarForm(response.POST or None, instance=instance)

        if form.is_valid():

            # Verificación de cita única
            unique = True
            for car in Car.objects.all():

                if (car.provider == form.cleaned_data['provider'] and
                        car.date == form.cleaned_data['date'] and
                        car.schedule == form.cleaned_data['schedule']):

                    unique = False
                    note = 'Horario no disponible'

            if unique:
                # Se guarda la modificación
                form.save()
                note = 'Modificado con éxito'

            return render(
                response,
                'views.html',
                {
                    'note': note
                }
            )

        return render(
            response,
            'change.html',
            {
                'carform': form,
                'pk': pk
            }
        )

    # Caso en el cual se selecciona el url crear cita
    else:

        # Se decide cual formulario mostrar
        if response.user.is_staff:
            new_form = CarStaffForm()
        else:
            new_form = CarForm()

        note = 'Ingrese los datos de su auto'

        if response.method == 'POST':

            if response.user.is_staff:
                filled_form = CarStaffForm(response.POST)
            else:
                filled_form = CarForm(response.POST)

            # Se verifica la validez del formulario
            if filled_form.is_valid() and response.user.is_authenticated:

                # Verificación de cita única
                repeated = False
                for car in Car.objects.all():

                    if (car.provider == filled_form.cleaned_data['provider']
                        and car.date == filled_form.cleaned_data['date']
                        and car.schedule == filled_form.cleaned_data[
                            'schedule']):

                        repeated = True

                if repeated:
                    note = 'El horario no está disponible'
                else:

                    new_car = filled_form.save()
                    if response.user.is_staff:
                        pass
                    else:

                        # Sólo se guardan las citas en los usuarios estándar
                        response.user.car.add(new_car)

                    note = (
                        'La cita se creó con éxito'
                    )
            else:
                note = 'Formulario inválido. Verifique el ingreso a su cuenta'
                'y los datos ingresados'

            return render(
                response,
                'create.html',
                {
                    'carform': new_form,
                    'note': note
                }
            )

        else:

            return render(
                response,
                'create.html',
                {
                    'note': note,
                    'carform': new_form
                }
            )


# Función view. Permite mostrar las citas prendientes de los usuarios estándar.
# Recibe el identificador único, del objeto con url seleccionado y, lo utiliza
# para desplegar los datos de ese objeto específico

def view(request, pk=None):

    # Si el usuario es administrativo, se redirecciona a su vista
    if request.user.is_staff:
        return redirect('staff')

    else:

        # Caso en el cual se se selecciona una cita específica
        if pk is not None:

            try:
                car = Car.objects.get(pk=pk)

            except Car.DoesNotExist:

                # Caso en el que el identificador ingresado  no corresponde
                # con ninguna cita registrada
                raise Http404('El auto con identificador {} no existe'
                              .format(pk))

            return render(
                request,
                'views.html',
                {
                    'pk': car.pk,
                    'brand': car.brand,
                    'car_model': car.car_model,
                    'year': car.year,
                    'schedule': car.schedule,
                    'date': car.date,
                    'provider_f_n': car.provider.first_name,
                    'provider_l_n': car.provider.last_name
                }
            )

        else:

            car_dict = {}

            for car in Car.objects.all():
                car_dict[car.pk] = {
                    'pk': car.pk,
                    'brand': car.brand,
                    'car_model': car.car_model,
                    'year': car.year,
                    'schedule': car.schedule,
                    'date': car.date
                }

            return render(
                request,
                'views.html',
                {
                    'car_dict': car_dict,
                }
            )


# Función home. Permite realizar la renderización del template index, el cual
# muestra la página de inicio y los urls a las demás páginas del proyecto

def home(response):
    return render(response, "index.html", {})


# Función available. Permite mostrar al usuario las citas que han sido
# registradas por todos los usuarios, a nombre de cualquier mecánico. Se
# despliegan ordenadas por mecánico y el objetivo es informar que no se
# encuentran disponibles

def available(response):

    # Se contruye un diccionario con los datos de los usuarios administrativos
    user_dict = {}

    for user in User.objects.all():

        if user.is_staff:

            user_dict[user.pk] = {
                'pk': user.pk,
                'user_name': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name
            }

    # Se contruye un diccionario con los datos de las citas registradas
    car_dict = {}

    for car in Car.objects.all():

        car_dict[car.pk] = {
            'pk': car.pk,
            'provider': str(car.provider),
            'date': car.date,
            'schedule': car.schedule
        }

    return render(
        response,
        'available.html',
        {
            'user_dict': user_dict,
            'car_dict': car_dict
        }
    )
