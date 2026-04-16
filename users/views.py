from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(
            username=username,
            password=password   
        )
        send_mail (
             subject="Hello, Thanks for signning up",
             message="Your account has been created successfully.",
             from_email="MedhaHMS <onboard@resend.dev>",
             recipient_list=[user.email],
             html_message="<strong>it works!</strong>",
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
