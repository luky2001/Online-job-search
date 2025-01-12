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
    context={'student':queryset}
    #return redirect('/show/')
    return render(request,'show.html',context)
def update(request, id):
    queryset = Student.objects.get(id=id)  # Retrieve the student object
    if request.method == "POST":
        data = request.POST
        stu_image = request.FILES.get('student_image')  # Get the new image (if provided)
        stu_name = data.get('student_name')  # Get the new name
        stu_age = data.get('student_age')  # Get the new age
        stu_address = data.get('student_address')  # Get the new address

        # Update the student fields
        queryset.name = stu_name
        queryset.age = stu_age
        queryset.address = stu_address

        # Update the image only if a new image is provided
        if stu_image:
            queryset.image = stu_image

        # Save the updated student object
        queryset.save()

        # Redirect to the show page after updating
        return redirect('/show/')

    # Pass the current student data to the template for editing
    context = {'student': queryset}
    return render(request, 'update.html', context)
