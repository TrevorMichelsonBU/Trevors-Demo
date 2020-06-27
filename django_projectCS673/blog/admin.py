from django.contrib import admin
from .models import Post

# Where we can register models to show up on admin page

admin.site.register(Post)


