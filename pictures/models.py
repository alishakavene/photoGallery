from django.db import models

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

    
    