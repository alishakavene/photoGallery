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
    category = models.ForeignKey('Category', null=True, blank=True,on_delete=models.CASCADE)
    

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

    @classmethod
    def get_category_list(self):
        k = self.category 
        
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]

class category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children',on_delete=models.CASCADE)

    class Meta:
       
        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"     

    def __str__(self):                           
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])

class ModelAdmin(models.Model):
    ...
    class Clipboard:
        js = ('clipboard.js',) 


    
    