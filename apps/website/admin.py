from django.contrib import admin

# Register your models here.

from .models import Data, DataStream

admin.site.register(Data)

admin.site.register(DataStream)
