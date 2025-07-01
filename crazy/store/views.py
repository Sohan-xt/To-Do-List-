from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import userdata
from store.models import taskdata


# Create your views here.
def test(request):
    return HttpResponse(':(')
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def index(request):
    return render(request,'index.html')
def todo(request):
    return render(request,'todo.html')

def registrations(request):
    return render(request,'registrations.html')
def signup(request):
    a=userdata()
    a.Name=request.GET['name']
    a.Email=request.GET['email']
    a.Password=request.GET['password']
    a.save()
    return render(request,'registrations.html')

def tododata(request):
    return render(request,'tododata.html')
def adddata(request):
    a=taskdata()
    a.Task=request.GET['task']
    a.Date=request.GET['date']
    a.Time=request.GET['time']
    a.save()
    return render(request,'tododata.html')

def login(request):
    return render(request,'login.html')
def log(request):    
    a=userdata.objects.filter(Email=request.GET['email'],Password=request.GET['password'])
    if a:
        return render(request,'tododata.html')
    else:
        return render(request,'login.html')

def show(request):
    a=taskdata.objects.all()
    return render(request,'show.html',{'data':a})

def delete(request,id):
    a=taskdata.objects.get(id=id)
    a.delete()
    return redirect('/show')

def edit(request,id):
    d=taskdata.objects.get(id=id)
    return render(request,'edit.html',{'x':d})

def editcode(request,id):
    d=taskdata.objects.get(id=id)
    d.Task=request.GET['Task']
    d.Date=request.GET['Date']
    d.Time=request.GET['Time']
    d.save()
    return redirect('../show')