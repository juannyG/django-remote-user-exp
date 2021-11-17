from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def login_view(request):
    if request.POST:
        user = authenticate(remote_user=request.POST['username'])
        if user is not None:
            login(request, user)
            return redirect('/secret1')

    return render(request, 'x/login.html', {})


@login_required
def secret_view_1(request):
    return render(request, 'x/secret1.html', {'user': request.user})


@login_required
def secret_view_2(request):
    return render(request, 'x/secret2.html', {'user': request.user})


def logout_view(request):
    logout(request)
    return redirect(settings.LOGIN_URL)
