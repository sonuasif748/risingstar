from django.shortcuts import render,redirect
from admin_dashboard import models
from publisher.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def homepage(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        user=request.user
        mv = add_categories.objects.filter(status=1)
        tm = mv.filter(language='Telugu')
        hm = mv.filter(language='Hindi')
        em = mv.filter(language='English')
        return render(request, 'homepage/home.html', {'user':user,'tm':tm, 'hm':hm, 'em':em})

@login_required(login_url='login')
def allmovies(request):
    user=request.user
    allm=add_categories.objects.filter(status=1)
    am=allm.filter(language='Telugu')
    return render(request, 'homepage/allmovies.html', {'user':user,'am':am })

@login_required(login_url='login')
def homeshows(request):
    return render(request,'homepage/homeshows.html')

@login_required(login_url='login')
def homekids(request):
    return render(request,'homepage/homekids.html')

@login_required(login_url='login')
def homeaction(request):
    return render(request,'homepage/homeaction.html')

@login_required(login_url='login')
def search(request):
    if request.method == "GET":
        search=request.GET.get('search')
        post=models.Movies.objects.all().filter(name=search)
        am = models.Movies.objects.all()
        return render(request, 'homepage/search.html', {'post':post, 'am': am})

@login_required(login_url='login')
def moviedetail(request, id):
    detail=add_categories.objects.get(pk=id)
    am=add_categories.objects.filter(status=1)
    return render(request, 'moviedetail.html', {'detail':detail, 'am':am})

def viewallpage(request,pk):
    a=add_categories.objects.filter(language=pk)
    return render(request, 'viewall.html',{'a':a})