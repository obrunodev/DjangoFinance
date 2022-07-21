from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from user.forms import SignInForm
from user.forms import SignUpForm


@login_required(login_url='user:signin')
def profile(request):
    return render(request, 'user/pages/profile.html')


def signin(request):
    # TODO Melhorar função de autenticação
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            try:
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username=username, password=password)

                if not username or not password:
                    messages.error(request, "Precisa preencher todos os campos!")
                    return redirect('user:signin')

                if user is not None:
                    login(request, user)
                    return redirect('user:profile')

                messages.error(request, "Erro ao logar. Tente novamente!")
                return redirect('user:signin')
            
            except User.DoesNotExist:
                messages.error(request, "Este usuário não existe! Crie uma conta para ter acesso.")
                return redirect('user:signin')
        
    if request.method == 'GET':
        form = SignInForm()
        context = {'form': form}
        return render(request, 'user/pages/signin.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user:profile')
        
        context = {'form': form}
        return render(request, 'user/pages/signup.html', context)
    
    if request.method == 'GET':
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'user/pages/signup.html', context)


def signout(request):
    logout(request)
    return redirect('user:signin')
