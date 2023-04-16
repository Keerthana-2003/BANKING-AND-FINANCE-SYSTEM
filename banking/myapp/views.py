import base64
from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Sum,Count

from .models import Transaction
from .forms import RegistrationData,ContactData, TransactionForm
import matplotlib.pyplot as plt
import io,urllib,base64
import numpy as np
import math
from .graphs import pieChart, barChart
# Create your views here.

def home(request):
    uname=User.objects.get(username=request.user.get_username())
    transactions = Transaction.objects.filter(username=uname)
    total_credit  = Transaction.objects.filter(username=uname).aggregate(Sum('credit_amount'))
    total_debit = Transaction.objects.filter(username=uname).aggregate(Sum('debit_amount'))
    if total_credit['credit_amount__sum'] is not None and total_debit['debit_amount__sum'] is not None:
        balanc = total_credit['credit_amount__sum'] - total_debit['debit_amount__sum']
    else:
        if total_debit['debit_amount__sum'] is None and total_credit['credit_amount__sum'] is None:
            balanc=0
        elif total_credit['credit_amount__sum'] is None and total_debit['debit_amount__sum'] is not None:
            balanc=total_credit['credit_amount__sum']
        else:
            balanc=0-total_debit['debit_amount__sum']
             
    balance = "{:.2f}".format(balanc)
    no_credit=[]   
    no_debit=[]
    for trans in transactions:
        if trans.credit_amount>0:
            no_credit.append(int(trans.credit_amount))
        elif trans.debit_amount>0:
            no_debit.append(int(trans.debit_amount))
    
    tc=total_credit['credit_amount__sum']
    td=total_debit['debit_amount__sum']
    tc = "{:.2f}".format(tc)
    td = "{:.2f}".format(td)
    return render(request, "home.html",{'balance':balance,'totalcredit':tc,'totaldebit':td})

def login2(request):
    return render (request,"login.html")
def landing(request):
    return render (request,"landing.html")
def contact(request):
    if request.method=='POST':
        form= ContactData(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"contact.html")
    else:
        form=ContactData()
    return render (request,"contact.html",{'form':form})
def sign(request):
     return render (request,"signin.html")
def payment(request):
            return render(request,"payment.html")
def trans(request):
    return render(request,"transaction.html")
def saving(request):
    return render(request,"saving.html")
def calender(request):
    return render(request,"calender.html")
def savings(request):
    return render(request,"savings.html")
def signup(request):
    if request.method=='POST':
        form= RegistrationData(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"login.html")
    else:
        form=RegistrationData()
    return render(request,'signup.html',{'form':form})

def login1(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username+" "+password)
        user = authenticate(request,username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("index")
    return render(request,'login.html')

def graph(request):   

    transactions = Transaction.objects.filter(username=request.user.get_username())
    no_credit=[]
    trans_cat_credit=[]
    trans_cat_debit=[]   
    no_debit=[]
    for trans in transactions:
        if trans.credit_amount>0 and trans.tran_category not in trans_cat_credit:
            no_credit.append(int(trans.credit_amount))
            trans_cat_credit.append(str(trans.tran_category))
        elif trans.tran_category in trans_cat_credit:  
            ind = trans_cat_credit.index(trans.tran_category)
            no_credit[ind] = int(no_credit[ind] + trans.credit_amount)
        elif trans.debit_amount>0 and trans.tran_category not in trans_cat_debit:
            no_debit.append(int(trans.debit_amount))
            trans_cat_debit.append(str(trans.tran_category))
        elif trans.tran_category in trans_cat_debit:
             ind = trans_cat_debit.index(trans.tran_category)
             no_debit[ind] = int(no_debit[ind] + trans.debit_amount)
    print(no_credit)
    print(no_debit)           
    p1=len(no_credit)
    p2=len(no_debit)
    # print(p1, p2)

    chart = pieChart(p1, p2)
    # bar = barChart(p1, p2)
    
 
    return render(request , 'graph.html', {"chart":chart})
    

# Create your views here.

def inserttrans(request):
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['username']=request.user.get_username()
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('index')
    else:
        form = TransactionForm()
    return render(request, "payment.html",{'form':form})