from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.

# Publisher views

def publisher_register(request):
    userform = PublisherUserForm()
    publisherform = PublisherForm()
    mydict = {'userform': userform, 'publisherform': publisherform}
    if request.method=="POST":
        userform = PublisherUserForm(request.POST)
        publisherform = PublisherForm(request.POST, request.FILES)
        if userform.is_valid() and publisherform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()
            publisher = publisherform.save(commit=False)
            publisher.user = user
            publisher.save()
            user.groups.add(Group.objects.get(name='publisher'))
            return redirect('/publisher')
    return render(request, 'publisher/publisherregister.html',context=mydict)

def is_publisher(user):
    return user.groups.filter(name='publisher').exists()

def publisher_login(request):
    if request.method == "POST":
        username = request.POST.get("publoginusername")
        password = request.POST.get("publoginpassword")
        User = authenticate(username=username, password=password)
        if User is not None :
            login(request, User)
            if is_publisher(request.user):
                return redirect('publisher')
            else:
                return redirect('publisher-login')
        else:
            return redirect('publisher-login')
    return render(request, 'publisher/publisherlogin.html')

@login_required(login_url='publisher-login')
def publisher(request):
    form=add_categories.objects.all()
    tm=form.filter(language='Telugu')
    hm=form.filter(language='Hindi')
    tem=form.filter(language='Tamil')
    mm=form.filter(language='Malayalam')
    km=form.filter(language='Kannada')
    em=form.filter(language='English')
    return render(request, 'publisher/publisher.html',{'form':form,'tm':tm,'hm':hm,'tem':tem,'mm':mm,'km':km,'em':em})

@login_required(login_url='publisher-login')
def pub_add_movie(request):
    if request.method == 'POST':
        form=pub_add_movie_form(request.POST, request.FILES)
        form.save()
        return redirect('/publisher')
    else:
        form = pub_add_movie_form()
        return render(request, '../templates/publisher/add_movies.html',{'form':form})

@login_required(login_url='publisher-login')
def pub_add_tm(request):
    if request.method == 'POST':
        form = pub_add_movie_form(request.POST, request.FILES)
        form.save()
        return redirect('/publisher')
    else:
        form = pub_add_movie_form()
    context = {
        'form': form
    }
    return render(request, '../templates/publisher/add_tolly_movies.html', context)

@login_required(login_url='publisher-login')
def pub_add_bm(request):
    if request.method == 'POST':
        form = pub_add_movie_form(request.POST, request.FILES)
        form.save()
        return redirect('/publisher')
    else:
        form = pub_add_movie_form()
    context = {
        'form': form
    }
    return render(request, '../templates/publisher/add_bolly_movies.html', context)

@login_required(login_url='publisher-login')
def pub_add_hm(request):
    if request.method == 'POST':
        form = pub_add_movie_form(request.POST, request.FILES)
        form.save()
        return redirect('/publisher')
    else:
        form = pub_add_movie_form
    context = {
        'form': form
    }
    return render(request, '../templates/publisher/add_holly_movies.html', context)

@login_required(login_url='publisher-login')
def moviesstatus(request):
    mv=add_categories.objects.all()
    return render(request,'publisher/moviestatus.html',{'mv':mv})

@login_required(login_url='publisher-login')
def pub_update_movie(request, id):
    pb = add_categories.objects.get(pk=id)
    pmu = pub_add_movie_form(instance=pb)
    ab = pub_add_movie_form(request.POST,request.FILES,instance=pb)
    if ab.is_valid():
        ab.save()
        ab.save()
        return redirect('/publisher')
    return render(request, 'publisher/updatemovie.html', {'form':pmu})

# def publisher_register(request):
#     if request.method == "POST":
#         email = request.POST.get('pubemail', '')
#         username = request.POST.get('pubusername', '')
#         password = request.POST.get('pubpassword', '')
#         pb = User.objects.create_user(username=username, email=email, password=password)
#         pb.groups.add(Group.objects.get(name='publisher'))
#         return redirect('/publisher')
#     return render(request, 'publisher/publisherregister.html')
