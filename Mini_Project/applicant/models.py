from django.db import models

class AppicantLogin(models.Model):

    User_name=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)


class ApplicantRegistration(models.Model):
    Name=models.CharField(max_length=40)
    Data_of_Birth=models.DateField(help_text="yyy-mm-dd")
    Email_ID=models.EmailField()
    Gender=models.CharField(max_length=30)
    Mobile_No=models.IntegerField(unique=True)
    Address=models.CharField(max_length=50)
    User_Name=models.CharField(max_length=30)
    Password=models.CharField(max_length=30)

class ApplicantApplication(models.Model):
    posts=(("developer","developer"),("tester","tester"),("manager","manager"),("hr","hr"))
    Name=models.CharField(max_length=40)
    Data_of_Birth=models.DateField(help_text="yyy-mm-dd")
    Email_ID=models.EmailField()
    Gender=models.CharField(max_length=30)
    Mobile_No=models.IntegerField(unique=True)
    Address=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    post=models.CharField(max_length=30,choices=posts)
    percentage=models.FloatField()
    resume_upload=models.FileField(upload_to='file_profiles')



