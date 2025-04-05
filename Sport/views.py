from django.shortcuts import render
from .forms import SportForm
from.models import Sports

# Create your views here.

def AllSport(request):
    sp_form=SportForm()
    allSpotys=Sports.objects.all().order_by('-created')
    
    context={
          'allSpoty':allSpotys,
    }
    return render(request, 'sports/view.html',context )