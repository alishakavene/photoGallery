from django.test import TestCase
from .models import Name,Image,tags
import datetime as dt

# Create your tests here.
class NameTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.food= Name(image_name = 'food')
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.food,Name))
    
     # Testing Save Method
    def test_save_method(self):
        self.food.save_name()
        names = Name.objects.all()
        self.assertTrue(len(names) > 0)

class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new name and saving it
        self.food= Name(image_name = 'food')
        self.food.save_name()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_image= Image(title = 'Test Article',post = 'This is a random test Post',image = self.food)
        self.new_image.save()

        self.new_image.tags.add(self.new_tag)

    def tearDown(self):
        Name.objects.all().delete()
        tags.objects.all().delete()
        Image.objects.all().delete()
    
    def test_get_photo_today(self):
        today_photo = Image.todays_photo()
        self.assertTrue(len(today_photo)>0)
    
    #........
    def test_get_photo_by_date(self):
        test_date = '2019-04-20'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        photo_by_date = Image.days_photo(date)
        self.assertTrue(len(photo_by_date) == 0)
