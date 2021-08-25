from django.shortcuts import render
from .models import *
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'polls/ui.html')

def artis(request):
    if request.method == 'POST':
        
        name=request.POST.get('artist_name')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        table=Artist(name=name,dob=dob,gender=gender)
        # breakpoint()
        table.save()
        return render(request,'polls/submit.html')

def awards(request):
    if request.method == 'POST':
        name=request.POST.get('award_name')
        date=request.POST.get('date')
        table=Award(name=name,date=date)
        table.save()
        return render(request,'polls/submit.html')

def movie(request):
    if request.method == 'POST':
        name=request.POST.get('movie_name')
        genre=request.POST.get('genre')
        release_date=request.POST.get('date')
        avg_rating=request.POST.get('avg_rating')
        language=request.POST.get('lang')
        duration=request.POST.get('duration')
        table=Movie(name=name,genre=genre,release_date=release_date,avg_rating=avg_rating,language=language,duration=duration)
        table.save()
        return render(request,'polls/submit.html')


def rates(request):
    if request.method == 'POST':
        movie=request.POST.get('movie')
        rate=request.POST.get('rate')
        votes=request.POST.get('votes')
        if movie == '3 idiots':
            no_of_votes=
        movies=Movie.objects.all()
        # context={'movie':movies}
        print(movies.votes)
        table=Rating(movie=movies,rate=rate,votes=votes)
        table.save()
        return render(request,'polls/submit.html', context)