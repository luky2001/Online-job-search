from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required

def home(request):
    if request.method == "POST":
        data = request.POST
        stu_image = request.FILES.get('student_image')
        stu_name = data.get('student_name')
        stu_age = data.get('student_age')
        stu_address = data.get('student_address')
        Student.objects.create(
            name=stu_name,
            age=stu_age,
            address=stu_address,
            image=stu_image  
        )
        return redirect('/show/')

    return render(request, 'student.html')
def delete(request,id):
    queryset=Student.objects.get( id=id)
    queryset.delete()
    return redirect('/show/')
def show(request):
    queryset = Student.objects.all()  # Get all students
    if request.GET.get('search'):
        print(request.GET.get('search'))
        queryset = queryset.filter(name__icontains=request.GET.get('search'))
    context = {'student': queryset}  # Define context outside the conditional block
    return render(request, 'show.html', context)

def update(request, id):
    queryset = Student.objects.get(id=id)  
    if request.method == "POST":
        data = request.POST
        stu_image = request.FILES.get('student_image')  
        stu_name = data.get('student_name')  
        stu_age = data.get('student_age')  
        stu_address = data.get('student_address')  
        queryset.name = stu_name
        queryset.age = stu_age
        queryset.address = stu_address
        if stu_image:
            queryset.image = stu_image
        queryset.save()
        return redirect('/show/')
    context = {'student': queryset}
    return render(request, 'update.html', context)

def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.info(request,"Invalid Username")
            return redirect('/login/')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Invalid Password ")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/show/')

    return render(request,'login.html')
def logout_page(request):
    logout(request)
    return redirect('/login/')
def register(request):
    if request.method =="POST":
        data=request.POST
        first_name=data.get('first')
        last_name=data.get('last')
        username=data.get('username')
        password=data.get('password')
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'Username already exist')
            return redirect('/register/')
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username)
        user.set_password(password)
        user.save()
        messages.info(request,'Account created successfully')
        return redirect('/register/')
    return render(request,'register.html')

def pro(request)
