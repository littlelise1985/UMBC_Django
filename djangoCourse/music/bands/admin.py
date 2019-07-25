from django.contrib import admin
# Register your models here.

from .models import Band, Member, Genre

# admin.site.register(MyModel)

admin.site.register(Band)
admin.site.register(Member)
admin.site.register(Genre)
