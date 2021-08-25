from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import MovieForm

# Create your views here.
def index(request):
    movies=Movie.objects.all()
    form=MovieForm(request.POST or None, request.FILES or None)
    if request.method=='POST':
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/polls/')
    else:
        context={'movies':movies,'form':form}
    return render(request,'polls/ui.html',context)

