from django.test import TestCase
from .models import Category, Book, Author

# Create your tests here.


class CategoryModelTest(TestCase):
    """ 
    Test for category model
    """
    def setUp(self):
        """  
        Set up non-modified objects used by all test methods
        """
        Category.objects.create(name='test', description='test')
    
    def test_category_name_is_not_blank(self):
        """ Test for category name is not blank """
        category = Category.objects.get(id=1)
        self.assertIsNot(category.name, '')
