from django.test import TestCase, TransactionTestCase
from .models import Image
from datetime import datetime
from django.contrib.auth.models import User

# Tests for the Profile model are in the user's app, test.py file

class ImageTest(TransactionTestCase): 
    '''
    
    declaring my test class as a TransactionTestCase rather than just TestCase. 
    Using the ormal TestCase throws a TransactionManagementError, when I try running 
    the gramApp application test, for Image model.

    However, deaclaring ImageTest as a TransactionTestCase fixes this problem
    
    '''
    def setUp(self):
        self.test_user = User(username='Mishi', password='new123')
        self.test_user.save()
        

        self.test_image = Image(image='media/default.png', caption='some text', author=self.test_user, uploadDate=datetime.now())


    def test_instance(self):
        self.assertTrue(isinstance(self.test_image, Image))

    def test_save(self):
        self.test_image.save_image()
        self.assertEqual(len(Image.objects.all()),1)

    def tearDown(self):
        self.test_user.delete()
        Image.objects.all().delete()
