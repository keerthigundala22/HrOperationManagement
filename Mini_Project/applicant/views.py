from django.shortcuts import render
from applicant.models import AppicantLogin
from django.views.generic.base import View
from .forms import ApplicantForm, ApplicantRegistrationForm, ApplicantApplicationForm


class ApplicantLogin(View):
    def get(self,request):
        return render(request,"applicantlogin.html",{"af":ApplicantForm})
    def post(self,request):
        b_name=request.POST["t1"]
        if b_name == "login":
            ef = ApplicantForm(request.POST)
            if ef.is_valid():
                ef.save()
                return render(request,"applicant1/applicant_anchor.html")
            else:
                pass


        else:
            pass


class ApplicantRegistration(View):
    def get(self,request):
        return render(request, "applicanthome.html",{"arf":ApplicantRegistrationForm})

    def post(self,request):
        b_name=request.POST["t2"]
        if b_name == "reg":
            ef = ApplicantRegistrationForm(request.POST)
            if ef.is_valid():
                ef.save()
                return render(request, "applicantapplicationlogin.html", {"af": ApplicantForm})
            else:
                pass


        else:
            pass


class Applicantionform(View):
    # def get(self,request):
    #     return render(request,"applicantapplicationlogin.html",{"af":ApplicantForm})
    def post(self,request):
        b_name=request.POST["t1"]
        if b_name=="login":
            ef = ApplicantForm(request.POST)
            if ef.is_valid():
                ef.save()
                return render(request,"applicantapplicationform.html",{"aaf":ApplicantApplicationForm()} )
            else:
                pass


        else:
            pass



