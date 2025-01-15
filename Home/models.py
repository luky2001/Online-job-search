from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=20,null=True)  
    age = models.IntegerField(null=True)            
    address = models.CharField(max_length=50,null=True)  
    image = models.FileField(upload_to="student", null=True, blank=True)

    def __str__(self):
        return self.name
