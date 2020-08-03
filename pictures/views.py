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


def show_category(request,hierarchy= None):
    category_slug = hierarchy.split('/')
    category_queryset = list(Category.objects.all())
    all_slugs = [ x.slug for x in category_queryset ]
    parent = None
    for slug in category_slug:
        if slug in all_slugs:
            parent = get_object_or_404(Category,slug=slug,parent=parent)
        else:
            instance = get_object_or_404(Post, slug=slug)
            breadcrumbs_link = instance.get_cat_list()
            category_name = [' '.join(i.split('/')[-1].split('-')) for i in breadcrumbs_link]
            breadcrumbs = zip(breadcrumbs_link, category_name)
            return render(request, "postDetail.html", {'instance':instance,'breadcrumbs':breadcrumbs})

    return render(request,"categories.html",{'post_set':parent.post_set.all(),'sub_categories':parent.children.all()})  

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"photogallery/image.html", {"image":image})  



