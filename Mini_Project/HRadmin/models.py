from django.db import models

class HRAdmin(models.Model):
    name=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)

class AddEmployee(models.Model):
    des=(('Manager','Manager'),('Developer','Developer'),('Tester','Tester'),('HR','HR'))


    Idno=models.IntegerField(primary_key=True)
    EmployeeName=models.CharField(max_length=30)
    Password=models.CharField(max_length=40)
    Designation=models.CharField(max_length=30,choices=des)
    Address=models.CharField(max_length=50)
    Email=models.EmailField()
    ContactNO=models.IntegerField()















