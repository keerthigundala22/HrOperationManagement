from django.shortcuts import render, redirect
from django.views.generic.base import View
from HRadmin.forms import HRadminForm,AddForm
from HRadmin.models import AddEmployee


class HRadmin(View):
    def get(self,request):
        return render(request,"admin.html",{"hr":HRadminForm()})
    def post(self,request):
        b_name = request.POST["t1"]
        if b_name == "admin":
            ef = HRadminForm(request.POST)
            if ef.is_valid():
                ef.save()
                return render(request,"adminhomepage.html")
            else:
                pass


        else:
            pass

class AddEmployeeDetails(View):
    def get(self,request):
        return render(request,"addemployee.html",{'eform':AddForm()})
    def post(self,request):
        b_name = request.POST["t2"]
        if b_name == "add":
            ef = AddForm(request.POST)
            if ef.is_valid():
                ef.save()
                return render(request, "adminhomepage.html")
            else:
                pass


        else:
            pass


class ViewEmployee(View):
    def get(self,request):
        add = AddEmployee.objects.all()
        return render(request,"viewemployee.html",{"add":add})


class UpdateEmployeeDetails(View):
    def get(self, request):
        update= AddEmployee.objects.all()
        return render(request, "updateemployee.html", {"up": update})
    def post(self,request):
        pass


class UpdateEmployee(View):
    def get(self,request):
        idno=request.GET['idno']
        x=AddEmployee.objects.get(Idno=idno)

        return render(request,"update.html",{'up':x})
    def post(self,request):
        id=request.POST["t1"]
        name=request.POST["t2"]
        des=request.POST["t3"]
        ad=request.POST["t4"]
        email=request.POST["t5"]
        con=request.POST["t6"]
        add=AddEmployee.objects.filter(Idno=id)
        add.update(EmployeeName=name,Designation=des,Address=ad,Email=email,ContactNO=con)
        return render(request,"adminhomepage.html")


class DeleteEmployee(View):
    def get(self, request):
        delete = AddEmployee.objects.all()
        return render(request, "deleteemployee.html", {"delete": delete})

    def post(self, request):
        pass



class Delete(View):
    def post(self, request):
        de=request.POST.getlist("c1")
        for x in de:
           d= AddEmployee.objects.filter(Idno=x).delete()
        return redirect('viewemployee')


