from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *


def all_yozuvchilar(request):
    if request.user.is_authenticated:
        data = {
            "yozuvchilar": Yozuvchi.objects.all()
        }
        return render(request, "muolif.html", data)
    else:
        return redirect('/login/')


def single_yozuvchi(request, pk):
    if request.user.is_authenticated:
        data = {
            'yozuvchi': Yozuvchi.objects.get(id=pk)
        }
        return render(request, "bitta_yozuvchi.html", data)
    else:
        return redirect('/login/')

def talaba(request):
    if request.method == 'POST':
        a = request.POST.get('username')
        b = request.POST.get('password')
        user = authenticate(username=a,password=b)
        if user == None:
            return redirect('/login/')
        else:
            login(request, user)



    if request.user.is_authenticated:
        data = {
            'Talabar': Talaba.objects.all()
        }
        return render(request,"Talaba.html",data)
    else:
        return redirect('/admin/')



def single_talaba(request, pk):
    if request.user.is_authenticated:
        data = {
            'bitta_talaba': Talaba.objects.get(id=pk)
        }
        return render(request, "bitta_talaba.html" ,data)
    else:
        return redirect('/login/')


def kitoblar(request):
    if request.user.is_authenticated:
        data = {
            'kitoblar': Kitob.objects.all()
        }
        return render(request,"kitoblar.html",data)
    else:
        return redirect('/login/')


def single_kitoblar(request,pk):
    if request.user.is_authenticated:
        data = {
            'kitob': Kitob.objects.get(id=pk)
        }
        return render(request, "single_kitob.html", data)
    else:
        return redirect('/login/')



def delete_talaba(request, pk):
    Talaba.objects.get(id=pk).delete()
    return redirect('/student/')


def delete_muolif(request, pk):
    Yozuvchi.objects.get(id=pk).delete()
    return redirect('/muolif/')


def delete_kitob(request,pk):
    Kitob.objects.get(id=pk).delete()
    return redirect('/Kitob/')


def create_talaba(request):
    a = request.POST['ism']
    b = request.POST['yosh']
    c = request.POST['kurs']
    Talaba.objects.create(ism=a,yosh=b,kurs=c)
    return redirect('/student/')

def create_muolif(request):
    a = request.POST['ism']
    b = request.POST['tirik']
    c = request.POST['tugilgan_yil']
    d = request.POST['millat']
    Yozuvchi.objects.create(ism=a,tirik=b,tugilgan_yil=c,millat=d)
    return redirect('/muolif/')

def create_kitob(request):
    a = request.POST['nom']
    b = request.POST['sahifa']
    c = request.POST['yil']
    d = request.POST['janr']
    Kitob.objects.create(nom=a,sahifa=b,yil=c,janr=d)
    return redirect('/Kitob/')


def RECORDS(request):
    data = {
        "ala": Records.objects.all()
    }
    return render(request,"record.html",data)

def login_now(request):
    return render(request,'login.html')




def logout_s(request):
    logout(request)
    return render(request,'login.html')


