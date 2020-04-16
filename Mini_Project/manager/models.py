from django.db import models

class ManagerModel(models.Model):
    UserName=models.CharField(max_length=30)
    Password=models.CharField(max_length=30)


class RecuirtmentModel(models.Model):
    OPPERTUNITY_CODE=models.IntegerField()
    QUALIFICATION=models.CharField(max_length=100)
    REGISTRATION_START_FROM=models.DateField(help_text="yyy-mm-dd")
    AGE_LIMT=models.IntegerField()
    LAST_DATE_TO_APPLY=models.DateField(help_text="yyy-mm-dd")
    DEPARTMENT_ID=models.IntegerField()
    NO_OF_POSITION=models.IntegerField()
    DESCRIPTION=models.CharField(max_length=200)
    RESPOSIBITIES=models.CharField(max_length=300)
    CONTACT_NO=models.IntegerField()

class Applicant(models.Model):
    Applicant_Id=models.IntegerField(print(True))
    Sellect_emp_Id=models.IntegerField(primary_key=True)
    Schedule_Date=models.DateField(help_text="yyy-mm-dd")

