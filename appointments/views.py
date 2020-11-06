from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Car
from .forms import CarForm
# 
# def new(request):
#     new_form = CarForm()
#     note= 'Hola perro'
#     return render(
#         request,
#         'new.html',
#         {
#             'note': note,
#             'carform': new_form,
#         }
#
#     )

def new(request):
    return HttpResponse('Showing "new" page')



def show(request, pk=None):

    if pk is not None:
        try:
            car=Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404('Pet with pk {} does not exist'.format(pk))
        return render(
            request,
            'show.html',
            {
                'object_pk': car.pk,
                'object_car_model': car.car_model,
                'object_year': car.year,
            }
        )

    else:
        car_dict = {}
        for car in Car.objects.all():
            car_dict[car.car_model]= {
                'pk': car.pk,
                'year': car.year,
            }
            print(car_dict)

        return render(
            request,
            'show.html',
            {
                'car_dict': car_dict,
            }
        )
