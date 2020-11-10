from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Car, ToDoList, Item
from .forms import CarForm, CreateNewList
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def staff(request, pk=None):
    if pk is not None:
        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404('Pet with pk {} does not exist'.format(pk))
        return render(
            request,
            'staff.html',
            {
                'object_brand': car.brand,
                'object_car_model': car.car_model,
                'object_year': car.year,
            }
        )

    else:
        car_dict = {}
        for car in Car.objects.all():
            car_dict[car.pk]= {
                'pk': car.pk,
                'brand': car.brand,
                'model': car.car_model,
                'year': car.year,
            }

        return render(
            request,
            'staff.html',
            {
                'car_dict': car_dict,
            }
        )


def base(request):
    return render(request,'base.html',{})


def new(request):
    return HttpResponse('Showing "new" page')



def show(request, pk=None):

    if pk is not None:
        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404('Pet with pk {} does not exist'.format(pk))
        return render(
            request,
            'show.html',
            {
                'object_brand': car.brand,
                'object_car_model': car.car_model,
                'object_year': car.year,
            }
        )

    else:
        car_dict = {}
        for car in Car.objects.all():
            car_dict[car.pk]= {
                'pk': car.pk,
                'brand': car.brand,
                'model': car.car_model,
                'year': car.year,
            }

        return render(
            request,
            'show.html',
            {
                'car_dict': car_dict,
            }
        )

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    if response.method == "POST":
        if response.POST.get("save"):
            for item in ls.item_set.all():
               if response.POST.get("c" + str(item.id)) == "clicked":
                   item.complete = True
               else:
                   item.complete = False

               item.save()

        elif response.POST.get("newItem"):
            txt= response.POST.get("new")
            if len(txt)>2:
                ls.item_set.create(text=txt, complete =False)
            else:
                print("invalid")

    return render(response, "index.html", {"ls": ls})


def create(response):
    new_form = CarForm()
    if response.method == 'POST':
        filled_form = CarForm(response.POST)

        if filled_form.is_valid() and response.user.is_authenticated:
            new_car = None
            repetido = False

            for car in Car.objects.all():
                
                if car.schedule == filled_form.cleaned_data['schedule']:
                    repetido = True
            if repetido:
                note='El horario no está disponible'
            else:
                new_car = filled_form.save()
                response.user.car.add(new_car)
                note = (
                    'Se creo una cita para un carro {} {} a las {}\n'
                    .format(new_car.brand, new_car.car_model,
                    new_car.schedule)
                )
        else:
            note='formulario inválido'
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
                'carform':new_form,
            }
        )


def view(response):
    return render(response, "views.html", {})

def home(response):
    return render(response, "home.html", {})
