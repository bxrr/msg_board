from django.db import models

class Post(models.Model): # creating a model class 
    text = models.TextField() # holds data text which is given by a TextField

    def __str__(self):
        return self.text[:50] # java equivalent of toString; data shown when Post is displayed directly