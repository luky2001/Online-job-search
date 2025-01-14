from django.shortcuts import render, redirect,get_object_or_404
from .models import *
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
    queryset=Student.objects.all()
    if request.GET.get('search'):
        print(request.GET.get('search'))
        queryset=queryset.filter(name__icontains=request.GET.get('search'))
        context={'student':queryset}
    return render(request,'show.html',context)
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

def profile
