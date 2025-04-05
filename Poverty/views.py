


from django.shortcuts import render
from.models import Povertyl

# Create your views here.

def Allpoverty(request):
    allSpoty=Povertyl.objects.all().order_by('-created')
    
    context={
        'all_poverty':allSpoty
          
    }
    return render(request, 'poverty/view.html',context )

