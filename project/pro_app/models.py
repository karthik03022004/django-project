from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=20, unique=True)
    emp_mail=models.EmailField(max_length=30)
    emp_pic=models.FileField(upload_to='media')
