from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Car
from .forms import CarForm, CarStaffForm
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User


@staff_member_required
def staff(request, pk=None):
    if pk is not None:
        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404('El auto con identificador {} no existe'.format(pk))
        return render(
            request,
            'staff.html',
            {
                'pk': car.pk,
                'user': car.user,
                'brand': car.brand,
                'car_model': car.car_model,
                'year': car.year,
                'schedule': car.schedule,
                'date': car.date,
                'provider': car.provider
            }
        )

    else:
        car_dict = {}
        for car in Car.objects.all():
            if request.user == car.provider:
                car_dict[car.pk]= {
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


def base(request):
    return render(request,'base.html',{})


def delete(response, pk=None):
    if pk is not None:
        instance = get_object_or_404(Car, pk=pk)
        instance.delete()
        return redirect('view')

    else:
        return redirect('view')


def create(response, pk=None):

    if pk is not None:
        instance = get_object_or_404(Car, pk=pk)
        form = CarForm(response.POST or None, instance=instance)

        if form.is_valid():
            unique=True

            for car in Car.objects.all():

                if (car.provider == form.cleaned_data['provider'] and
                        car.date == form.cleaned_data['date'] and
                        car.schedule == form.cleaned_data['schedule']):

                    unique=False
                    note = 'Horario no disponible'

            if unique:
                form.save()
                note = 'Modificado con éxito'

            return render(
                response,
                'views.html',
                {
                    'note':note
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
    else:
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

            if filled_form.is_valid() and response.user.is_authenticated:
                repetido = False

                for car in Car.objects.all():

                    if (car.provider == filled_form.cleaned_data['provider'] and
                        car.date == filled_form.cleaned_data['date'] and
                        car.schedule == filled_form.cleaned_data['schedule']):

                        repetido = True

                if repetido:
                    note = 'El horario no está disponible'
                else:
                    new_car = filled_form.save()
                    if response.user.is_staff:
                        pass
                    else:
                        response.user.car.add(new_car)
                    note = (
                        'La cita se creó con éxito'
                    )
            else:
                note='Formulario inválido. Verifique el ingreso a su cuenta y los datos ingresados'
            return render(
                response,
                'create.html',
                {
                    'carform':new_form,
                    'note': note
                }
            )
        else:
            return render(
                response,
                'create.html',
                {
                    'note': note,
                    'carform':new_form
                }
            )


def view(request, pk=None):

    if request.user.is_staff:
        return redirect('staff')
    else:

        if pk is not None:
            try:
                car = Car.objects.get(pk=pk)
            except Car.DoesNotExist:
                raise Http404('El auto con identificador {} no existe'.format(pk))
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
                    'provider': car.provider
                }
            )

        else:
            car_dict = {}
            for car in Car.objects.all():
                car_dict[car.pk]= {
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


def home(response):
    return render(response, "home.html", {})


def available(response):

    user_dict = {}
    for user in User.objects.all():

        if user.is_staff:
            user_dict[user.pk]= {
                'pk': user.pk,
                'user_name': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name
            }

    car_dict = {}
    for car in Car.objects.all():

        car_dict[car.pk]= {
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
