from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import appointmentForm,departmentForm,patientForm,DoctorForm
from .models import appointment,department,patientregistration,DoctorRegistration,login
from django.contrib.auth.models import User,auth
# Create your views here.






def home(request):
    return render(request,'home.html')

def base(request):
    return render(request,'base.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        
    

        try:
            user = patientregistration.objects.get(username=username,password=password)

            if user is not None:
                print(user)
                return render(request, 'usermodule.html')
            return render(request, 'login.html')
        except:
            print("hello")
            pass
        try:
            user = User.objects.get(username=username, password=password)
            print(user)
            if user is not None:
                print(user)
                return render(request, 'home.html')
                # return render(request,'Adminmodule.html')
        except:
            print("hi1")
            pass

        try:
            user = DoctorRegistration.objects.get(username=username,password=password)

            print(user)
            if user is not None:
                print(user)
                return render(request, 'doctormodule.html')
            return render(request, 'login.html')
        except:
            print("helllooooo")
            pass

    else:
     return render(request,'login.html')




def patientregistration1(request):
    if request.method == "POST":
        form =patientForm(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                return redirect('patientregistration')
            if form.is_valid():
                form.save()
                user = User.objects.create_user(username=username, password=password)
                user.save()
        else:
            return redirect('patientregistration')
        return redirect('/')
    else:
        return render(request,'patientregistration.html')




def DoctorRegistration1(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                return redirect('DoctorRegistration')
            if form.is_valid():
                form.save()
                user = User.objects.create_user(username=username,password=password)
                user.save()
        else:
            return redirect('DoctorRegistration')
        return redirect('/')
    else:
        return render(request,'DoctorRegistration.html')

def appointment1(request):
    dlist = DoctorRegistration.objects.all()
    dtlist = department.objects.all()
    if request.method=="POST":
        form=appointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        form=appointmentForm()
    return render(request,'appointment.html',{'dlist':dlist,'dtlist':dtlist})

def contact(request):
    return render(request,'contact.html')
def doctormodule(request):
    return render(request,'doctormodule.html')
def usermodule(request):
    return render(request,'usermodule.html')
def About(request):
    return render(request,'About.html')


def viewappointment(request):
    result =appointment.objects.all()
    return render(request,'viewappointment.html',{'result':result})

def edit_appointment(request,id):
    data=department.objects.all()
    data1=DoctorRegistration.objects.all()
    result =appointment.objects.get(id=id)
    context={
        "data":data,
        "data1":data1,
        "result":result,
    }
    return render(request,'edit_appointment.html', {'context':context})

def deleteappointment(request,id):
    result=appointment.objects.get(id=id)
    result.delete()
    return redirect('/viewappointment.html')


def updateappointment(request, id):
    result=appointment.objects.get(id=id)
    form=appointmentForm(request.POST, instance=result)
    if form.is_valid():
        form.save()
        return redirect('/viewappointment')
    return render(request, 'edit_appointment.html', {'result':result})



def departmentreg(request):
    if request.method=="POST":
        form=departmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        form=departmentForm()
        return render(request,'departmentreg.html')

def viewdepartment(request):
    result=department.objects.all()
    return render(request,'view_department.html',{'result':result})

def editdepartment(request,id):
    result=department.objects.get(id=id)
    return render(request,'editdepartment.html',{'result':result})

def deletedepartment(request):
    result=department.objects.all()
    result.delete()
    return render('/view_department.html')

def updatedepartment(request,id):
    result=department.objects.get(id=id)
    form=departmentForm(request.POST,instance=result)
    if form.is_valid():
        form.save()
        return redirect('/view_department')
    return render(request,'editdepartment.html',{'result':result})



def view_doctor(request):
    result = DoctorRegistration.objects.all()
    return render(request,'view_doctor.html',{'result':result})

def edit_doctor(request,id):
    result=DoctorRegistration.objects.get(id=id)
    return render(request,'edit_doctor.html',{'result':result})

def delete_doctor(request):
    result=DoctorRegistration.objects.all()
    result.delete()
    return render('/view_doctor.html')

def update_doctor(request,id):
    result=DoctorRegistration.objects.get(id=id)
    form=DoctorForm(request.POST,instance=result)
    if form.is_valid():
        form.save()
        return redirect('/view_doctor')
    return render(request,'edit_doctor.html',{'result':result})

def view_patient(request):
    return render(request,'view_patient.html')
def edit_patient(request):
    return render(request,'edit_patient.html')
def delete_patient(request):
    return render(request,'delete_patient.html')

