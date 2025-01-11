from django.shortcuts import render, redirect
from .models import *

def home(request):
    if request.method == "POST":
        data = request.POST
        stu_image = request.FILES.get('student_image')
        stu_name = data.get('student_name')
        stu_age = data.get('student_age')
        stu_address = data.get('student_address')
        
        # Create a new Student record
        Student.objects.create(
            name=stu_name,
            age=stu_age,
            address=stu_address,
            image=stu_image  
        )

        return redirect('/')
    
   
    queryset = Student.objects.all()
    context = {'student': queryset}

    return render(request, 'student.html', context)

def delete
