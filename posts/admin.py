from django.contrib import admin

from .models import Post # import Post model

admin.site.register(Post) # register Post model within the admin database so it can be seen and edited