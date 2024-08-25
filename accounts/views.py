from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            print('user authenticated')
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else: 
        return render(request, 'login.html')

def logout_page(request):
    auth.logout(request)
    return redirect('/')
    
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email exists')
                return redirect('register')
            
            else:    
                u = User.objects.create_user(
                    username=user_name,
                    password=password1, 
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )
                
                u.save()
                print('# User has been saved')
                return redirect('login')
        else:
            messages.info(request, 'Password mismatch')
            return redirect('register')
        
        return redirect('/')    
    else:    
        print('hello hehe')
        return render(request, 'register.html')    

    