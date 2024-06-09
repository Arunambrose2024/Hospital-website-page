from django.contrib import admin
from .models import appointment
from .models import department,DoctorRegistration,patientregistration,login
# Register your models here.




admin.site.register(appointment)
admin.site.register(department)
admin.site.register(DoctorRegistration)
admin.site.register(patientregistration)
admin.site.register(login)
