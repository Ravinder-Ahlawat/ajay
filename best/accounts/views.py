from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import pubg_info
# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        pubg_id = request.POST['pubg_id']
        pubg_username = request.POST['pubg_username']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('Register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('Register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                messages.info(request, 'User created')
                return redirect('/')
            
        else:
            messages.info(request, 'pass not matching...')
            return redirect('Register')
        return redirect('/')
        
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")

        else:
            messages.info(request, 'no data found plz create account')
            return redirect('Register')

    else:
        messages.info(request, 'no data found plz create account')
        return redirect('Register')


def logout(request):
    auth.logout(request)
    return redirect('/')


def aj(request, user):
    if request.method == 'POST':
        user = request.POST['user']
        pubg_id = request.POST['pubg_id']
        pubg_username = request.POST['pubg_username']
        mobile_no = request.POST['mobile']
        clan = request.POST['clan_name']
        info = pubg_info(user=user, pubg_id=pubg_id, pubg_username=pubg_username, mobile_no=mobile_no, clan=clan)
        info.save()
        messages.info(request, 'profile updated')
        return render(request, 'login.html')
        
    else:
        infos = pubg_info.objects.filter(user=user)
        print(infos[0])
        return render(request, 'login.html', {'infos':infos[0]})
    
