from django.shortcuts import render
from .models import *

# Create your views here.

'''def unwind(request):
    mood = Mood.objects.all()
    music = Music.objects.all()
    context={'music' : music, 'mood' : mood}
    return render(request, 'Unwind/unwind.html', context)'''
def unwind(request):
    mood_id = request.GET.get('mood_id')
    if mood_id:
        songs = Music.objects.filter(m_id=mood_id)
    else:
        songs = Music.objects.filter(m_id=1)
    mood = Mood.objects.all()
    context = {'songs': songs, 'mood': mood}
    return render(request, 'Unwind/unwind.html', context)