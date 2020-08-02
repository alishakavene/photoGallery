from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to Picha a web application that allows the users to post and interact with diffrent kinds of pictures')