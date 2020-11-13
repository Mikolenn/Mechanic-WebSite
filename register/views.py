from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from .forms import RegisterForm, RegisterStaffForm
from django.http import HttpResponseRedirect

# Create your views here.

# def register(response):
#     if response.method == "POST":
#         form=RegisterForm(response.POST)
#         if form.is_valid():
#             form.save()
#         return redirect("/")
#     else:
#         form=RegisterForm()
#
#     return render(response, "register/register.html", {"form":form})

def register (request):

    form = RegisterForm (request.POST)

    if form.is_valid():
        form.save()
        return redirect('/')

    else:
        form = RegisterForm()

        args = {'form' : form }
    return render(request , "register/register.html" , args)

def registerStaff(request):

    form = RegisterStaffForm (request.POST)

    if form.is_valid():
        form.save()
        return redirect('/')

    else:
        form = RegisterStaffForm ()

        args = {'form' : form }
    return render(request , "register/register.html" , args)
