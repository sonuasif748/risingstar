from django.shortcuts import render
from admin_dashboard.models import *
from publisher.models import *


# Create your views here.

def home(request):
    user = request.user
    mv = add_categories.objects.filter(status=1)
    tm = mv.filter(language='Telugu')
    hm = mv.filter(language='Hindi')
    em = mv.filter(language='English')
    tem = mv.filter(language='Tamil')
    mm = mv.filter(language='Malayalam')
    a=mv.filter(geners='Action')
    ad=mv.filter(geners='Adventure')
    c=mv.filter(geners='Comedy')
    h=mv.filter(geners='Horror')
    t=mv.filter(geners='Thirller')
    d=mv.filter(geners='Drama')
    s=mv.filter(geners='Sci Fi')
    return render(request, 'index.html', {'user': user, 'tm': tm, 'hm': hm, 'em': em,'tem':tem,'mm':mm,
                                          'a':a,'ad':ad,'c':c,'h':h,'t':t,'d':d,'s':s})


def movies(request):
    user = request.user
    tm = Tollywood_Movie.objects.all()
    bm = Bollywood_Movie.objects.all()
    hm = Hollywood_Movie.objects.all()
    return render(request, 'movies.html', {'user': user, 'tm': tm, 'bm': bm, 'hm': hm})


def shows(request):
    return render(request, 'shows.html')


def kids(request):
    return render(request, 'kids.html')


def action(request):
    return render(request, 'action.html')


def contact(request):
    return render(request, 'contact.html')


def search(request):
    if request.method == "GET":
        search = request.GET.get('search')
        post = add_categories.objects.all().filter(title=search)
        am = add_categories.objects.all()
        return render(request, 'searchbar.html', {'post': post, 'am': am})


