from django.contrib import admin
from .models import Books,BookStatus

# Register your models here.
admin.site.register(Books)
admin.site.register(BookStatus)
