from django.shortcuts import redirect, render
from .models import *
from .forms import *
import datetime
# Create your views here.


def index(request):
    """
    Add the index page
    """
    return render(request, 'reward/add_reward.html')


def artists(request):
   """
   Add the Artists
   """
   form = ArtistForm
   if request.method == 'POST':
       add_artist = ArtistForm(request.POST)
       if add_artist.is_valid():
           add_artist.save()
           return render(request, 'reward/artists.html', {'form': form})

   return render(request, 'reward/artists.html', {'form': form})


def awards(request):
    """
    Add the awards
    """
    form = AwardForm
    if request.method == 'POST':
       add_awards = AwardForm(request.POST)
       if add_awards.is_valid():
           add_awards.save()
           return render(request, 'reward/awards.html', {'form': form})

    return render(request, 'reward/awards.html', {'form': form})


def movies(request):
    """
    Add the movies
    """
    form = MovieForm
    if request.method == 'POST':
       add_movies = MovieForm(request.POST)
       if add_movies.is_valid():
           add_movies.save()
           return render(request, 'reward/movies.html', {'form': form})

    return render(request, 'reward/movies.html', {'form': form})


def topten(req):
    """
    Show top ten rated movies
    """
    movies = Movie.objects.all().order_by('-avg_rating')[:10]
    return render(req, 'reward/display.html', {"context": movies})


def leastten(req):
    """
    Show ten least rated movies
    """
    movies = Movie.objects.all().order_by('avg_rating')[:10]
    return render(req, 'reward/display.html', {"context": movies})


def date_sort(request):
    """
    function to sort movies within a range of date
    """
    if request.POST:
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']
        # breakpoint()
        movies = Movie.objects.filter(release_date__range=[from_date, to_date])
        context = {'movies': movies}
    else:
        movies = Movie.objects.none()
        context = {'movies': movies}
    return render(request, 'reward/date_sort.html', context)



def rate_movie(request):
    """
    Rate the movie and increment the votes
    """
    form = RatingForm
    if request.method == 'POST':
        add_rating = RatingForm(request.POST)
        if add_rating.is_valid():
           add_rating.cleaned_data
           form_object=add_rating.save(commit=False)
           form_object.movie=add_rating.cleaned_data.get('movie')
           form_object.rate=add_rating.cleaned_data.get('rate')
           filter_data=Rating.objects.filter(movie=form_object.movie,rate=form_object.rate)
           if filter_data.count() >= 1:
               rate_obj=filter_data.get()
               rate_obj.votes+=1
               rate_obj.save()
           else:
                form_object.votes=1
                form_object.save()
                form_object.movie.save()

           # Logic to add avg_rating to movie table 
           movie=Movie.objects.get(name=form_object.movie)
           rating_obj=Rating.objects.filter(movie=movie)
           rating_list=[int(rating_data.votes)*int(rating_data.rate) for rating_data in rating_obj]
           vote_list=[rating_data.votes for rating_data in rating_obj]
           movie.avg_rating=sum(rating_list)/sum(vote_list)
           movie.save()

           return render(request,'reward/votes.html',{'form':form})

    return render(request,'reward/rating.html',{'form':form})

def search_movie(request):
    """
    Search the movie by artist or movie name
    """
    form = SearchForm(request.POST or None)
    queryset = None
    if request.method == 'POST':
        queryset = Movie.objects.filter(name__icontains=form['name'].value(
        )) or Movie.objects.filter(artists__aname=form['name'].value())
        print(queryset)
    context = {
        "form": form,
        "queryset": queryset}
    return render(request, 'reward/search.html', context)
