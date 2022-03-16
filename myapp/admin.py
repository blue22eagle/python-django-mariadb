from django.contrib import admin

# Register your models here.
from .models import myTable

admin.site.register(myTable)
