from django import forms
from .models import appointment,department,patientregistration,DoctorRegistration,login






class appointmentForm(forms.ModelForm):
    class Meta:
        model=appointment
        fields="__all__"
        widget={}


class departmentForm(forms.ModelForm):
    class Meta:
        model=department
        fields="__all__"
        widget={

        }

class patientForm(forms.ModelForm):
    class Meta:
        model = patientregistration
        fields = "__all__"
        widget = {

                }
class DoctorForm(forms.ModelForm):
    class Meta:
        model = DoctorRegistration
        fields = "__all__"
        widget = {

                }

class loginForm(forms.ModelForm):
    class Meta:
        model = login
        fields = "__all__"
        widget = {

                }

