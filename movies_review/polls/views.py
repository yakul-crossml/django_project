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
        # movie=request.POST.get('movie')
        # rate=request.POST.get('rate')
        # votes=request.POST.get('votes')
        sum=int(0)
        a=0
        data=Rating.objects.all()
        for ke in data:
            movie=ke.movie.name
            print(movie)
            # breakpoint()
            # con={'key':data}
            # print("INSIDE IF ")
            # for key in data:
            if movie == "3 idiots":
                # for key in data:
                k=ke.rate
                a=a+1
                sum=k+sum
        avg=sum/a
        print(avg)



        
        # d


        # movies=Movie.objects.all()
        # # context={'movie':movies}
        # print(movies.votes)
        # table=Rating(movie=movies,rate=rate,votes=votes)
        # table.save()
        return render(request,'polls/submit.html')