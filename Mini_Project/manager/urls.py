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
from HRadmin import urls as HRadmin
from manager import views

urlpatterns = [
    path('manager/',views.Manager.as_view(),name="manager"),
    path('recuirtment/',views.Recuirtment.as_view(),name="recuirtment"),
    path('recuirtment_details/',views.RecuirtmentDetails.as_view(),name="recuirtment_details"),
    path('modifydetails/',views.ModifyDetails.as_view(),name="modifydetails"),
    path('modify/',views.Modify.as_view(),name="modify"),
    path('deletedetails/', views.DeleteDetails.as_view(), name="deletedetails"),
    path('deletee/', views.Deletee.as_view(), name="deletee"),
    path('applicantopen/', views.ApplicantOpen.as_view(), name="applicantopen"),


]
