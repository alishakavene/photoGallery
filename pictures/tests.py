from django.test import TestCase
from .models import Name,Image,tags

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
