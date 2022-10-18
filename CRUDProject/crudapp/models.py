import email
from django.db import models

# Create your models here.
class StudentModel(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=40)
    contact=models.IntegerField()
    fees=models.FloatField()
    emailid=models.EmailField()
    password=models.CharField(max_length=60)
    photo=models.ImageField(upload_to='student_images/')
