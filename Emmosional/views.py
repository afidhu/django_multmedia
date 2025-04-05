from django.shortcuts import render
from.models import Emmosionaly

# Create your views here.

def AllEmossion(request):
    allEmoss=Emmosionaly.objects.all().order_by('-created')
    
    context={
        'all_Emoss':allEmoss
          
    }
    return render(request, 'emmosion/view.html',context )