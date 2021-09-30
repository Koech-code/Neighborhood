from django.contrib.auth.models import User
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .forms import NewUserForm, NeighborhoodForm,PostForm,ProfileForm
from django.contrib.auth import login
from django.contrib import messages
from .email import send_welcome_email
from .models import Post, Profile
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    neighborhoods=Neighborhood.objects.all()

    return render(request, 'home/index.html', {'neighborhoods':neighborhoods})


@login_required(login_url='/accounts/login/')
def neighborhood(request, id):

    neighborhoods=Neighborhood.objects.filter(id=id)
    business=Business.objects.filter(neighborhood_id=id)
    post=Post.objects.filter(neighborhood=id)


    return render(request, 'hoods.html', {'neighborhoods':neighborhoods, 'business':business, 'post':post})


def join_hood(request, id):
    neighborhood = Neighborhood.objects.get(id=id)
    request.user.profile.neighborhood = neighborhood
    request.user.profile.save()

    return HttpResponseRedirect(request.path_info)

def leave_hood(request, id):
    leave=Neighborhood.objects.get(id=id)
    request.user.profile.neighborhood=None
    request.user.profile.save()
    
    return redirect('home')


def profile(request):
    current_user=request.user  
    profile=Profile.objects.filter(user=current_user)
    return render(request, 'profile.html',  {'profile':profile})


@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method=='POST':
        profile_form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,('Your profile is successfully updated'))
            return redirect('/')
        else:
            messages.error(request,('please correct errror below'))
    else:
        profile_form=ProfileForm(instance=request.user.profile)
    
    return render(request, 'update_profile.html', {'profile_form':profile_form})


@login_required(login_url='/accounts/login/')
def create_post(request, hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user
            post.save()
            return redirect('/', hood.id)
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})

def business(request):

    business=Business.objects.all()

    return render(request, 'business.html',{'business':business})

@login_required(login_url='/accounts/login/')
def business_search(request):
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_business = Business.objects.filter(name__contains=search_term)
        business=Business.objects.all()
        print(business)
        message = f"{search_term}"
        print(searched_business)
        array=[]
        for searched_business in searched_business:
            searched_business=Business.objects.get(id=searched_business.id)
            array.append(searched_business)
        return render(request, 'search.html',{"message":message,"results": array})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

