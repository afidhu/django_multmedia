from django.shortcuts import render
from.models import Educations

# Create your views here.

def Alleducation(request):
    allEducat=Educations.objects.all().order_by('-created')
    
    context={
        'all_Education':allEducat
          
    }
    return render(request, 'education/view.html',context )
