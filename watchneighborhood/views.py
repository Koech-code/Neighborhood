from watchneighborhood.models import Neighborhood
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .forms import NewUserForm
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


def profile(request, user):
    
    return redirect(request, 'profile.html')