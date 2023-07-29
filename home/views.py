from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import passengerdetail
def Home(request):
    if request.method=='POST':
        unname=request.POST.get('unname')
        unname01=request.POST.get('unname01')
        unname02=request.POST.get('unname02')
        return redirect('signup')
    return render(request,'Home.html')
def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        password=request.POST.get('password')

        new_user=User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name

        )
        new_user.set_password(password)
        new_user.save()
        return redirect('login')
    return render(request,'signup.html')
def login(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        pword=request.POST.get('pword')

        user=auth.authenticate(username=uname,password=pword)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            return redirect('invalid')
    return render(request,'login.html')
def dashboard(request):
    if request.method=='POST':
        pname=request.POST.get('pname')
        des=request.POST.get('des')
        num=request.POST.get('num')
        pnum=request.POST.get('pnum')
        tnum=request.POST.get('tnum')
        
        new_note=passengerdetail.objects.create(
            passengername=pname,
            Destination=des,
            Tickets=num,
            Phonenumber=pnum,
            Trainnumber=tnum

        )
        new_note.save()
        return redirect('passengerinfo')
    user=request.user
    paramerters={
        "user":user,
    }
    return render(request,'dashboard.html',paramerters)
def passengerinfo(request):
    user=request.user
    passengerinfo=passengerdetail.objects.all()

    paramerters={
        "user":user,
        "passengerinfo":passengerinfo
    }
    return render(request,'passengerinfo.html',paramerters)
def edit(request,id):
    note=passengerdetail.objects.get(id=id)
    if request.method=='POST':
        pname=request.POST.get('pname')
        des=request.POST.get('des')
        num=request.POST.get('num')
        pnum=request.POST.get('pnum')
        
        note.passengername=pname
        note.Destination=des
        note.Tickets=num
        note.Phonenumber=pnum
        note.save()
        return redirect('passengerinfo')
    return render(request,'edit.html')
def delete(request, id):
    note=passengerdetail.objects.get(id=id)
    note.delete()
    return redirect('passengerinfo')
def logout(request):
    auth.logout(request)
    return redirect("login")
def invalid(request):
    return render(request,'invalid.html')
    
    
        
