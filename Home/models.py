from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20,null=True)  # Removed the trailing comma
    age = models.IntegerField(null=True)            # Removed the trailing comma
    address = models.CharField(max_length=50,null=True)  # Removed the trailing comma
    image = models.FileField(upload_to="student", null=True, blank=True)

    def __str__(self):
        return self.name
