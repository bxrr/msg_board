from django.urls import reverse
from django.test import TestCase

from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just a test') # creating an instance of Post with given text parameter
    
    def test_text_context(self): # all testing functions need to start with test[_]
        # line below sets var post to the post object created in set up
        post = Post.objects.get(id=1) # next post will be set to id=2 and so on (identifiable)
        expected_object_name = str(post.text) # gets the post var's text data and stores it in var
        self.assertEqual(expected_object_name, 'just a test') # compares actual to expected for error

class HomePageView(TestCase):
    def setUp(self):
        Post.objects.create(text='another test') # instance of Post created with data in param

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/') # virtual client opens page at '/' (data assigned to resp)
        self.assertEqual(resp.status_code, 200) # if page status code is equal to 200, page exists

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home')) # finds url with name 'home' 
        self.assertEqual(resp.status_code, 200) # if status code is 200, url with name 'home' exists

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home')) 
        self.assertEqual(resp.status_code, 200) # runs previous test
        self.assertTemplateUsed(resp, 'home.html') # then tests if template used by 'home' is correct