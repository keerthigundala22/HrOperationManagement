from django.shortcuts import render, redirect
from django.views.generic.base import View
from manager.forms import ManagerForm,RecuirtmentForm
from manager.models import RecuirtmentModel


class Manager(View):
    def get(self,request):
        return render(request,"manager_login.html",{"mf":ManagerForm()})
    def post(self,request):
        b_name = request.POST["t1"]
        if b_name == "manager":
            ef = ManagerForm(request.POST)
            if ef.is_valid():
                ef.save()
                return render(request,"managerhomepage.html")
            else:
                pass


        else:
            pass


class Recuirtment(View):
     def get(self,request):
         return render(request,"recuirtment.html")


class RecuirtmentDetails(View):
    def get(self,request):
        return render(request,"recuirtment_details.html",{"rd":RecuirtmentForm()})
    def post(self,request):
        b_name=request.POST["t1"]
        if b_name=="recuirtment":
            rf=RecuirtmentForm(request.POST)
            if rf.is_valid():
                rf.save()
                return render(request,"manager/recuirtment_home.html")
            else:
                pass
        else:
            pass


class ModifyDetails(View):
    def get(self,request):
        qs=RecuirtmentModel.objects.all()
        return render(request,"modifydetails.html",{"data":qs})
    def post(self,request):
        id=request.POST['m1']
        qs= RecuirtmentModel.objects.get(OPPERTUNITY_CODE=id)
        return render(request,"modifybutton.html",{"data":qs,"rf":RecuirtmentForm})


class Modify(View):
    def get(self,request):
        pass
    def post(self,request):
        oc=request.POST["t1"]
        qu=request.POST["t2"]
        re=request.POST["t3"]
        ag=request.POST["t4"]
        last=request.POST["t5"]
        did=request.POST["t6"]
        no=request.POST["t7"]
        des=request.POST["t8"]
        res=request.POST["t9"]
        con=request.POST["t10"]
        add=RecuirtmentModel.objects.filter(OPPERTUNITY_CODE=oc)
        add.update(QUALIFICATION=qu,REGISTRATION_START_FROM=re, AGE_LIMT=ag,LAST_DATE_TO_APPLY=last,DEPARTMENT_ID=did,  NO_OF_POSITION=no, DESCRIPTION=des,
         RESPOSIBITIES=res,CONTACT_NO=con)
        return render(request,"manager/recuirtment_home.html")


class DeleteDetails(View):
    def get(self, request):
        data=RecuirtmentModel.objects.all()
        return render(request, "manager/deletedetails.html", {"data":data})


class Deletee(View):
    def post(self,request):
       de= request.POST.getlist("d1")
       for x in de:
          d= RecuirtmentModel.objects.filter(OPPERTUNITY_CODE=x).delete()
       return redirect("recuirtment")


class ApplicantOpen(View):
    def get(self,request):
        return render(request,"applicantopen.html")
