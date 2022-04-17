from django.http import HttpResponse
from app.models import Leaderboard
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

def home(request):
    template = loader.get_template('app/home.html')
    return HttpResponse(template.render({}, request))

def space_invaders(request):
    template = loader.get_template('app/space_invaders.html')
    return HttpResponse(template.render({}, request))

def leaderboard(request):
    template = loader.get_template('app/leaderboard.html')
    context = { 'leaderboard': Leaderboard.objects.all().order_by('-score') }
    return HttpResponse(template.render(context, request))



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
