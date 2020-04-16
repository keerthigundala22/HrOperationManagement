"""Mini_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from HRadmin import views

urlpatterns = [
    path('HRadmin/',views.HRadmin.as_view(),name="HRadmin"),
    path('addemployee/',views.AddEmployeeDetails.as_view(),name="addemployee"),
    path('viewemployee/',views.ViewEmployee.as_view(),name="viewemployee"),
    path('updateemployeedetails/',views.UpdateEmployeeDetails.as_view(),name="updateemployeedetails"),
    path('update/',views.UpdateEmployee.as_view(),name="updateemployee"),
    path('deleteemployee/',views.DeleteEmployee.as_view(),name="deleteemployee"),
    path('delete/',views.Delete.as_view(),name="delete"),

]
