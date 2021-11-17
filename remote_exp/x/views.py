from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def login_view(request):
    error = None
    if request.POST:
        user = None
        if request.POST.get('remote_username'):
            '''
            This workflow must be incredibly buttoned up.

            If a user exists with a username/password, this workflow lets them
            in with NO PASSWORD CHALLENGE!
            '''
            user = authenticate(remote_user=request.POST['remote_username'])
        elif request.POST.get('username') and request.POST.get('password'):
            user = authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )

        if user is not None:
            login(request, user)
            return redirect('/secret1')
        else:
            error = 'authentication failed'

    return render(request, 'x/login.html', {'message': error})


@login_required
def secret_view_1(request):
    return render(request, 'x/secret1.html', {'user': request.user})


@login_required
def secret_view_2(request):
    return render(request, 'x/secret2.html', {'user': request.user})


def logout_view(request):
    logout(request)
    return redirect(settings.LOGIN_URL)
