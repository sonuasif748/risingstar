from django.shortcuts import render, HttpResponse, redirect,HttpResponseRedirect
from .forms import *
from admin_dashboard.models import *
from publisher.models import *
from publisher.forms import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from user.forms import *

# Admin Views

def dashboardlogin(request):
    if request.method == "POST":
        username = request.POST.get("adminusername")
        password = request.POST.get("adminpassword")
        User = authenticate(username=username, password=password)
        if User is not None:
            login(request, User)
            return redirect("/dashboard")
        else:
            return redirect('/')
    return render(request, 'dashboard/dashboardlogin.html')

def dashlogout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='dashboardlogin')
def dashboard(request):
    if request.user.is_anonymous:
        return redirect('/dashboardlogin')
    if request.user.is_superuser:
        form = add_categories.objects.all()
        tm = form.filter(language='Telugu')
        hm = form.filter(language='Hindi')
        tem = form.filter(language='Tamil')
        mm = form.filter(language='Malayalam')
        km = form.filter(language='Kannada')
        em = form.filter(language='English')
        return render(request, '../templates/dashboard/dashboard.html', {'tm': tm, 'hm': hm, 'tem': tem,'mm':mm,'km':km,'em':em})
    else:
        return redirect('/')


@login_required(login_url='dashboardlogin')
def add_movie(request):
    return render(request, '../templates/dashboard/add_movies.html')

@login_required(login_url='dashboardlogin')
def add_tm(request):
    if request.method == 'POST':
        form=pub_add_movie_form(request.POST, request.FILES)
        form.save()
        return redirect('/dashboard')
    else:
        form = pub_add_movie_form()
    context = {
        'form': form
    }
    return render(request, '../templates/dashboard/add_tolly_movies.html', context)

@login_required(login_url='dashboardlogin')
def add_bm(request):
    if request.method == 'POST':
        form=pub_add_movie_form(request.POST, request.FILES)
        form.save()
        return redirect('/dashboard')
    else:
        form = pub_add_movie_form()
    context = {
        'form': form
    }
    return render(request, '../templates/dashboard/add_bolly_movies.html', context)

@login_required(login_url='dashboardlogin')
def add_hm(request):
    if request.method == 'POST':
        form=pub_add_movie_form(request.POST, request.FILES)
        form.save()
        return redirect('/dashboard')
    else:
        form = pub_add_movie_form()
    context = {
        'form': form
    }
    return render(request, '../templates/dashboard/add_holly_movies.html', context)

@login_required(login_url='dashboardlogin')
def movieslist(request):
    user = request.user
    am = Movies.objects.all().order_by('id')
    paginator = Paginator(am, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, '../templates/dashboard/movieslist.html', {'user':user,'page_obj':page_obj })

@login_required(login_url='dashboardlogin')
def library(request):
    am = Movies.objects.all()
    return render(request, 'dashboard/library.html', {'am':am })


@login_required(login_url='dashboardlogin')
def update_movie(request, id):
    ud = Movies.objects.get(pk=id)
    am = add_movie_form(instance=ud)
    ab = add_movie_form(request.POST,request.FILES,instance=ud)
    if ab.is_valid():
        ab.save()
        return redirect('/library' or '/movieslist')
    return render(request, 'dashboard/updatemovie.html', {'form':am})


@login_required(login_url='dashboardlogin')
def delete_movie(request, id):
    if request.method == 'POST':
        dl = Movies.objects.get(pk=id)
        dl.delete()
        return HttpResponseRedirect('/library')


@login_required(login_url='dashboardlogin')
def usersmodify(request):
    userslist=User.objects.all()
    return render(request, 'dashboard/users.html',{'users':userslist})

@login_required(login_url='dashboardlogin')
def createuser(request):
    userform = CustomerUserForm()
    customerform = CustomerForm()
    mydict = {'userform': userform, 'customerform': customerform}
    if request.method == "POST":
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
        return redirect('/usersmodify')
    return render(request, 'dashboard/createuser.html', context=mydict)

@login_required(login_url='dashboardlogin')
def update_user(request, id):
    upuser = User.objects.get(pk=id)
    upa = CustomerUserForm(instance=upuser)
    upb = CustomerForm(instance=upuser)
    if request.method == "POST":
        upd1 = CustomerUserForm(request.POST,instance=upuser)
        upd2 = CustomerForm(request.POST,instance=upuser)
        if upd1.is_valid() and upd2.is_valid():
            upd1.save()
            upd2.save()
            return redirect('/usersmodify')
    return render(request, 'dashboard/updateuser.html', {'form1':upa,'form2':upb})

@login_required(login_url='dashboardlogin')
def delete_user(request, id):
    deluser = User.objects.get(pk=id)
    deluser.delete()
    return HttpResponseRedirect('/usersmodify')

@login_required(login_url='dashboardlogin')
def published_movies(request):
    mv=add_categories.objects.all()
    if request.method=="POST":
        form=pub_admin_changestatus(request.POST)
        form.save()
        return redirect('/published_movies')
    else:
        form = pub_admin_changestatus()
    return render(request,'dashboard/published_movies.html',{'mv':mv,'form':form})

@login_required(login_url='dashboardlogin')
def admin_pub_status_update(request,id):
    pb = add_categories.objects.get(pk=id)
    pmu = pub_admin_changestatus(instance=pb)
    ab = pub_admin_changestatus(request.POST, request.FILES, instance=pb)
    if ab.is_valid():
        ab.save()
        ab.save()
        return redirect('/published_movies')
    return render(request, 'dashboard/pub_statusupdate.html', {'form': pmu})


@login_required(login_url='dashboardlogin')
def pub_update_movie(request, id):
    pb = add_categories.objects.get(pk=id)
    pmu = pub_admin_movie_form(instance=pb)
    ab = pub_admin_movie_form(request.POST,request.FILES,instance=pb)
    if ab.is_valid():
        ab.save()
        ab.save()
        return redirect('/published_movies')
    return render(request, 'dashboard/pub_updatemovie.html', {'form':pmu})

@login_required(login_url='dashboardlogin')
def pub_delete_movie(request, id):
    if request.method == 'POST':
        dl = add_categories.objects.get(pk=id)
        dl.delete()
        return HttpResponseRedirect('/published_movies')

def update_status(request,status,id):
    add_categories.objects.filter(id=id).update(status=status)
    return redirect('/published_movies')