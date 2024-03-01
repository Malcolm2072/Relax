from django.shortcuts import render

# Create your views here.
def relive(request):
    return render(request, 'Relive/relive.html')