from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image

# Create views here.
def welcome(request):
    return HttpResponse(request, 'welcome.html')

def todays_photo(request):
    photo = Image.todays_photo()
    return render(request, 'photogallery/today-photos.html', { "photo":photo})

# View Function to present photo from past days


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'photogallery/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any photo"
        return render(request, 'photogallery/search.html',{"message":message})
    



