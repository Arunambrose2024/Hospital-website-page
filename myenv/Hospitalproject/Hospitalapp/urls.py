"""
URL configuration for Hospitalproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('base', views.base, name='base'),

    path('login',views.login,name='login'),
    path('patientregistration',views.patientregistration1,name='patientregistration'),
    path('DoctorRegistration',views.DoctorRegistration1,name='DoctorRegistration'),
    path('appointment',views.appointment1,name='appointment'),
    path('contact',views.contact,name='contact'),
    path('doctormodule',views.doctormodule,name='doctormodule'),
    path('usermodule',views.usermodule,name='usermodule'),
    path('About',views.About,name='About'),
    path('departmentreg',views.departmentreg,name='departmentreg'),

    path('viewappointment',views.viewappointment,name='viewappointment'),
    path('edit_appointment/<int:id>', views.edit_appointment, name='edit_appointment'),
    path('updateappointment/<int:id>', views.updateappointment, name='updateappointment'),
    path('deleteappointment/<int:id>', views.deleteappointment, name='deleteappointment'),

    path('view_department',views.viewdepartment,name='view_department'),
    path('editdepartment/<int:id>', views.editdepartment, name='editdepartment'),
    path('updatedepartment/<int:id>', views.updatedepartment, name='updatedepartment'),
    path('deletedepartment/<int:id>', views.deletedepartment, name='deletedepartment'),

    path('view_doctor',views.view_doctor,name='view_doctor'),
    path('view_patient',views.view_patient,name='view_patient'),
]
