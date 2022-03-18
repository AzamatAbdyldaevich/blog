from django.contrib import admin
from .models import *

admin.site.register(Author)
admin.site.register(Image)
admin.site.register(Blog)
admin.site.register(Hashtag)

