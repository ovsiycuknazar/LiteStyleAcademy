from .models import Video
from django.shortcuts import render

# Create your views here.
def index(request):
    video=Video.objects.all()
    return render(request,"index.html",{"video":video})