from django.db import models
import datetime as dt

@classmethod
def todays_photo(cls):
        today = dt.date.today()
        photo = cls.objects.filter(post_date__date = today)
        return photo
@classmethod
def days_photo(cls,date):
        photo = cls.objects.filter(post_date__date = date)
        return photo


# Create your models here.
class Name(models.Model):
    image_name = models.CharField(max_length =40)

    def __str__(self):
        return self.image_name

    def save_name(self):
        self.save()


class tags(models.Model):
    name = models.CharField(max_length =40)

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length =60)
    description = models.TextField()
    name = models.ForeignKey(Name,on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    post_date = models.DateTimeField(auto_now_add=True)
    image_image = models.ImageField(upload_to = 'images/')

    @classmethod
    def todays_photo(cls):
        today = dt.date.today()
        photo = cls.objects.filter(post_date__date = today)
        return photo
    @classmethod
    def days_photo(cls,date):
        photo = cls.objects.filter(post_date__date =date)
        return photo


    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news


    
    