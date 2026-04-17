from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
import resend
from django.conf import settings

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(
            username=username,
            password=password
        )
        resend.api_key = settings.RESEND_API_KEY
        resend.Emails.send(
        {
            'from'   : 'onboard@resend.dev',
            'to'     :['bannenollashekar@gmail.com'],
            'subject': 'Welcome to Medha Hospital Management System',
            'html'   : f"<h1>Welcome {user.username}</h1><p>We are glad to have you on board!</p>"
        }
        )
        print(f'sent email to {user.email}')
        login(request, user)
        return redirect('/dashboard')
    else:
        return render(request, 'user_signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('/login')
