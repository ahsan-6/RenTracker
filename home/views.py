from turtle import home
from django.shortcuts import render,redirect,reverse
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm , editRenterForm, editPropertyForm

from .models import Properties, Renter, Transaction
from django.contrib.auth.models import User
import datetime

# Create your views here.

# func to register a user
def registerUser(request):
    if request.method == 'POST':
        regForm = NewUserForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            login(request,authenticate(username = regForm.username,password = regForm.password1))
            return redirect('home')
    context = {'form':NewUserForm}
    return render(request, 'register.html',context)

# func to log user in
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"Account does not exist")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username and password don't match.")
    return render(request, 'login.html')

# function to log user out
def logoutUser(request):
    logout(request)
    return redirect('login')

# Renter functions

# func to display renters
@login_required(login_url="login")
def renterDetails(request):
    renterDueData = Renter.objects.filter(user = request.user).filter(dateLeft = None).filter(balance__lt = 0).only('id','name','balance').order_by('balance')
    for i in renterDueData:
        i.balance = -i.balance
    renterData = Renter.objects.filter(user = request.user).filter(dateLeft = None).filter(balance__gte = 0).only('id','name','balance')
    context = { 'renterData' : renterData,'renterDueData':renterDueData}
    return render(request,'home.html', context)

# func to add renter
@login_required(login_url="")
def addRenter(request):
    context = {'propData':Properties.objects.filter(user = request.user).only('id','address','occupied')}
    if request.method == 'POST':
        ren = Renter()
        ren.name = request.POST.get('name')
        ren.user = request.user 
        ren.homeAddr = request.POST.get('homeAddr')
        ren.phNo = request.POST.get('phNo')
        ren.email = request.POST.get('email')
        ren.dateJoined = request.POST.get('dateJoined')
        if (ren.name=="" or ren.homeAddr=="" or len(ren.phNo)!=10 or ren.email=="" or ren.dateJoined==""):
            messages.error(request,"Invalid input!")
            return redirect('add renter')

        ren.property = Properties.objects.get(id = int(request.POST.get('propertyId')))
        ren.property.occupied = True
        ren.property.save()
        ren.save()
        
        return redirect('home')
    else:

        return render(request,'add renter.html',context)

# func to edit renter details
@login_required(login_url="login")
def editRenter(request,pk):
    # context = {'renterData':Renter.objects.get(id = pk)}
    renter = Renter.objects.get(id = pk)
    form = editRenterForm(instance=renter)
    if request.method == 'POST':
        form = editRenterForm(request.POST,instance=renter)
        if form.is_valid():
            form.save()
            return redirect(reverse('renter',args=pk))

    context = {'form':form}

    return render(request,'edit renter.html',context)

    

# func to display renter details
@login_required(login_url="login")
def renter(request, pk):
    renterData = Renter.objects.get(id = pk)
    transData = Transaction.objects.filter(renter_id = pk).order_by('-date')
    context = {'renterData':renterData,'transData':transData}
    return render(request, 'renter.html',context)


# Property functions

# func to display properties 
@login_required(login_url="login")
def propertyDetails(request):
    context = {'propData' : Properties.objects.filter(user = request.user)}
    return render(request,'property details.html',context)

# func to add properties
@login_required(login_url="login")
def addProperty(request):
    if request.method == 'POST':
        pro = Properties()
        pro.user = request.user
        pro.address = request.POST.get('address')
        pro.rent = request.POST.get('rent')
        pro.propType = request.POST.get('propType')
        if (len(pro.address)==0):
            messages.error(request, "Address field can't be empty!")
            return redirect('add property')
        if (pro.rent==''):
            messages.error(request, "Invalid rent!")
            return redirect('add property')

        pro.save()
        return redirect('property details')
    else:
        return render(request,'add property.html')

# func to display property details
@login_required(login_url="login")
def property(request,pk):
    propData = Properties.objects.get(id = pk)
    if (propData.occupied == True):
        renterData = Renter.objects.get(property = pk)
        context = {'propData':propData,'renterData':renterData}
    else:
        context = {'propData':propData}

    return render(request, 'property.html',context)

# func to edit property details
@login_required(login_url="login")
def editProperty(request,pk):
    prop = Properties.objects.get(id = pk)
    form = editPropertyForm(instance=prop)
    if request.method == 'POST':
        form = editPropertyForm(request.POST,instance=prop)
        if form.is_valid():
            form.save()
            return redirect(reverse('property',args=pk))
    context = {'form':form}
    return render(request,'edit property.html',context)

# Transactions functions

# function to display transactions
@login_required(login_url="login")
def transactionDetails(request):
    sixMonthsAgo = datetime.date.today() - datetime.timedelta(weeks = 26)
    transData = Transaction.objects.filter(renter__in = Renter.objects.filter(user = request.user).only('id')).filter(dues__isnull=True).filter(date__gt = sixMonthsAgo).order_by('-date')
    context = {'transData':transData}
    return render(request, 'transaction details.html',context)

# function to add transaction
@login_required(login_url="")
def addTransaction(request):
    context = {'renterData':Renter.objects.filter(user = request.user).only('id','name')}
    if request.method == 'POST':
        tra = Transaction()
        tra.renter = Renter.objects.get(id = request.POST.get('renterId'))
        
        option = request.POST.get('option')
        if (option == 'payment'):
            tra.paid = int(request.POST.get('paid'))
            if tra.paid<=0:
                messages.error(request,"invalid amount!")
                return redirect('add transaction')
            tra.renter.balance += tra.paid
            tra.balance = tra.renter.balance
        else:
            tra.dues = int(request.POST.get('paid'))
            if tra.dues<=0:
                messages.error(request,"invalid amount!")
                return redirect('add transaction')
            tra.renter.balance -= tra.dues
            tra.balance = tra.renter.balance
        tra.date = request.POST.get('date')
        if tra.date=="":
            messages.error(request,"Invalid date!")
            return redirect('add transaction')

        tra.renter.save()
        tra.save()
        #as soon as renter is added add transaction for rent due with joindate/todays date
        return redirect('transaction details')
    else:

        return render(request, 'add transaction.html',context)


# function to change password
@login_required(login_url="login")
def changePassword(request):
    if request.method == 'POST':
        currPass = request.POST.get("currPass")
        username = request.user.username
        user = authenticate(username = username, password = currPass)
        if user is not None:
            newPass1 = request.POST.get("newPass1")
            newPass2 = request.POST.get("newPass2")
            if newPass1 != newPass2:
                messages.error(request,"New passwords don't match!")
                return redirect ('change password')
            else:
                u = User.objects.get(username=username)
                u.set_password(newPass1)
                u.save()
                user = authenticate(username=username,password=newPass1)
                login(request,user)
                messages.success(request,"Password changed.")
                return redirect ('change password')

        else:
            messages.error(request,"Current password is incorrect!")
            return redirect ('change password.html')

    return render(request,'change password.html')

