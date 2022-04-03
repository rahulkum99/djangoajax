from django.shortcuts import render
from .forms import StudentRegistration
from . models import User
from django.http import JsonResponse
# Create your views here.

def index(request):
    form = StudentRegistration()
    std = User.objects.all()

    return render(request,'index.html',{'form':form,'std':std})


def save_data(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            stuid = request.POST['stuid']
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if stuid == "":
                usr = User(name=name,email=email,password=password)
            else:
                usr =User(id=stuid,name=name,email=email,password=password)
            usr.save()
            stud = User.objects.values()
            print(stud)
            studlist = list(stud)
            return JsonResponse({'status':'save','student_data':studlist})
        else:
            return JsonResponse({'status':0})


def delete_data(request):
    if request.method == "POST":
        id  = request.POST['sid']
        print(id)
        pi =User.objects.get(pk =id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        student = User.objects.get(pk=id)
        student_data = {
            'id':student.id,'name':student.name,'email':student.email,'password':student.password
        }
        return JsonResponse(student_data)
    else: 
        pass