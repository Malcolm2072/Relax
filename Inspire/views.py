from django.shortcuts import render
from .models import *

# Create your views here.

def inspire(request):
    story_id = request.GET.get('story_id')
    if story_id:
        info = Story.objects.filter(p_id=story_id)
    else:
        info = Story.objects.filter(p_id=1)
    story= Story.objects.all()
    context={'story' : story, 'info' : info}
    return render(request, 'Inspire/inspire.html',context)
