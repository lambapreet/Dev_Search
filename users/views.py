from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


# Create your views here.

def loginUser(request):
    
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'username does not exits')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('proifles')
        else:
            messages.error(request,'Incorrect value')
            
    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.error(request,'user logout!')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request,'Created!')
            
    context = {'page':page, 'form':form}
    return render(request, 'users/login_register.html',context)

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'users/profile.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    
    topSkills = profile.skill_set.exclude(description__exact='')  
    otherSkills = profile.skill_set.filter(description='')
    context = {'profile':profile, 'topskills':topSkills, 'otherskills':otherSkills}
    return render(request, 'users/user-profile.html', context)