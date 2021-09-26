from watchneighborhood.models import Business, Neighborhood, Profile
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .forms import NewUserForm, NeighborhoodForm,PostForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, authenticate #add this
from .email import send_welcome_email


# Create your views here.
def index(request):
    return render(request, 'index.html')

def neighborhood(request):
    neighborhoods=Neighborhood.objects.all()

    return render(request, 'hoods.html', {'neighborhoods':neighborhoods})



def join_hood(request, id):
    neighborhood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighborhood = neighborhood
    request.user.profile.save()

    return redirect('hood')

def leave_hood(request, id):
    leave=get_object_or_404(Neighborhood, id)
    request.user.profile.neighborhood=None
    request.user.profile.save()
    
    return redirect('hood')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect('/accounts/login/')    


def create_hood(request):
    if request.method == 'POST':
        form = NeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('hood')
    else:
        form = NeighborhoodForm()
    return render(request, 'newhood.html', {'form': form})

def create_post(request, hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            return redirect('/', hood.id)
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})

def business(request):

    business=Business.objects.all()

    return render(request, 'business.html',{'business':business})

def business_search(request):
    if request.method == 'GET':
        name = request.GET.get("title")
        results = Business.objects.filter(name__icontains=name).all()
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'search.html', params)
    else:
        message = "You haven't searched for any business"
    return render(request, "search.html")

