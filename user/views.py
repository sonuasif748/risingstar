from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import authenticate
from django.contrib.auth import login,logout
from .forms import *
from django.contrib import messages
from publisher.models import *

# Create your views here.

def register(request):
    userform = CustomerUserForm()
    customerform = CustomerForm()
    mydict = {'userform': userform, 'customerform': customerform}
    if request.method=="POST":
        userform = CustomerUserForm(request.POST)
        customerform = CustomerForm(request.POST, request.FILES)
        if userform.is_valid() and customerform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()
            customer = customerform.save(commit=False)
            customer.user = user
            customer.save()
            user.groups.add(Group.objects.get(name='customer'))
            return redirect('/')
    return render(request, 'users/register.html',context=mydict)

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get("loginusername")
        password = request.POST.get("loginpassword")
        User = authenticate(username=username, password=password)
        if User is not None:
            login(request, User)
            return redirect("/")
        else:
            return redirect('/')
    return render(request, 'users/login.html')

def logoutuser(request):
    logout(request)
    return redirect('/')

def test(request):
    user = request.user
    mv = add_categories.objects.filter(status=1)
    tm = mv.filter(language='Telugu')
    hm = mv.filter(language='Hindi')
    em = mv.filter(language='English')
    tem = mv.filter(language='Tamil')
    mm = mv.filter(language='Malayalam')
    a = mv.filter(geners='Action')
    ad = mv.filter(geners='Adventure')
    c = mv.filter(geners='Comedy')
    h = mv.filter(geners='Horror')
    t = mv.filter(geners='Thirller')
    d = mv.filter(geners='Drama')
    s = mv.filter(geners='Sci Fi')
    return render(request, 'test.html', {'user': user, 'tm': tm, 'hm': hm, 'em': em, 'tem': tem, 'mm': mm,
                                          'a': a, 'ad': ad, 'c': c, 'h': h, 't': t, 'd': d, 's': s})