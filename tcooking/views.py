from django.shortcuts import render
from . import models
from django.db.models import CharField, Count,Sum
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import TemplateView 
# from django.conf import settings
# from django.core.files.storage import FileSystemStorage
# from django.views.generic.base import TemplateView
# Create your views here.
def index(request):
    masuk=False
    if request.user.is_authenticated:
        masuk=True
    resep=models.recipe.objects.all()
    prev=models.rekomend.objects.all()
    out1={
        'rec':resep,
        'reck':prev,
        'masuk':masuk,
    }
    return render(request, 'index.html',out1)
def about(request):
    masuk=False
    if request.user.is_authenticated:
        masuk=True
    ot={
    	'masuk':masuk
    }
    return render(request, 'about.html',ot)
def menu(request):
    masuk=False
    if request.user.is_authenticated:
        masuk=True
    resep=models.recipe.objects.all()
    menulist={
        'listres':resep,
        'masuk':masuk,
    }
    return render(request, 'menu.html',menulist)
def detail(request,id):
    masuk=False
    if request.user.is_authenticated:
        masuk=True
    resep2=models.recipe.objects.filter(id=id).first()
    out2={
        'resep2':resep2,
        'masuk':masuk,
    }
    return render(request, 'chef.html',out2)
    
def detailrekomen(request,id):
    masuk=False
    if request.user.is_authenticated:
        masuk=True
    rekom2=models.rekomend.objects.filter(id=id).first()
    out3={
        'rekom2':rekom2,
        'masuk':masuk,
    }
    return render(request, 'detailrekom.html',out3)

def favor(request,id):
    masuk=False
    if request.user.is_authenticated:
        masuk=True
    pilihan=models.recipe.objects.filter(id=id).first()
    
    temp=request.user.id
    if request.method == 'POST':
       models.favorit.objects.create(
        no_fav=temp,
        nama=pilihan.nama,
        foto=pilihan.foto,
        video=pilihan.video,
        keterangan=pilihan.keterangan,
        resep=pilihan.resep,
       )
    out4={
        'resep2':pilihan,
        'masuk':masuk,
    }
    return render(request, 'chef.html',out4)

def favorc(request,id):
    masuk=False
    if request.user.is_authenticated:
        masuk=True
    pilihan2=models.rekomend.objects.filter(id=id).first()
    
    temp=request.user.id
    if request.method == 'POST':
       models.favorit.objects.create(
        no_fav=temp,
        nama=pilihan2.nama,
        foto=pilihan2.foto,
        video=pilihan2.video,
        keterangan=pilihan2.keterangan,
        resep=pilihan2.resep,
       )
    out5={
        'rekom2':pilihan2,
        'masuk':masuk,
    }
    return render(request, 'detailrekom.html',out5)

def profil(request):
    masuk=False
    if request.user.is_authenticated:
        masuk=True
    fvf=models.favorit.objects.filter(no_fav=request.user.id)
    prev2=models.rekomend.objects.all()
    
    tmp = 0
    for z in fvf:
         tmp += 1
    out1={
        'fv':fvf,
        'reck2':prev2,
        'masuk':masuk,
        'jml':tmp
    }
    return render(request, 'userpage.html',out1)



# Login & regist ===============================================================
@login_required
def special(request):
    print(user_type)
    return HttpResponse("Berhasil Login !")
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    ret = {
        'user_form':user_form,
        'registered':registered
       }
    return render(request,'registration.html',ret)

def user_login(request):
    masuk=False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                masuk=True
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})

# Bagian Search ====================================================================
class SearchView(TemplateView):
    template_name = 'menu2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lw = self.request.GET.get('katakunci')
        resulth = models.recipe.objects.filter(
            Q(nama__contains=lw))
        print(resulth)
        context = {
            "resulth":resulth,
        }
        return context