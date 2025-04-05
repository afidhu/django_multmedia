from django.shortcuts import render
from.models import EnterTimentaly

# Create your views here.

def entertaim(request):
    allEnter=EnterTimentaly.objects.all().order_by('-created')
    
    context={
        'all_Enter':allEnter
          
    }
    return render(request, 'entertaiment/view.html',context )
