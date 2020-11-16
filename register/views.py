from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from .forms import RegisterForm, RegisterStaffForm


# Función register. Permite el registro de los usuarios estándar

def register(request):

    form = RegisterForm(request.POST)

    if form.is_valid():

        form.save()
        return redirect('/')

    else:

        form = RegisterForm()
        args = {'form': form}

    return render(request, "register/register.html", args)


# Función registerStaff. Permite el registro de los usuarios administrativos
# @staff_member_required
def registerStaff(request):

    if request.user.is_staff:

        form = RegisterStaffForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/')

        else:

            form = RegisterStaffForm()
            args = {'form': form}

        return render(request, "register/register.html", args)

    return redirect('/register')


# Función logoutuser. Permite a cualquier usuario cerrar la sesión

def logoutuser(request):

    print('Loggin out {}'.format(request.user))

    do_logout(request)
    print(request.user)

    return render(request, "logout/logoutuser.html", {})
