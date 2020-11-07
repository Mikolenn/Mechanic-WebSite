from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect


from .models import Car, ToDoList, Item
from .forms import CarForm, CreateNewList
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

def base(request):
    return render(request,'base.html',{})


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

def index(request, id):
    ls = ToDoList.objects.get(id=id)
    if request.method == "POST":
        if request.POST.get("save"):
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

    return render(request, "index.html", {"ls": ls})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid() and response.user.is_authenticated:
            n=form.cleaned_data["name"]
            t=ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
        # return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()

    return render(response,"create.html",{"form":form})


def view(response):
    return render(response, "views.html", {})

def home(response):
    return render(response, "home.html", {})
