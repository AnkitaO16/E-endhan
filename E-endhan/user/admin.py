from django.contrib import admin
from .models import Contact, Destination

# Register your models here.
admin.site.register(Destination),
admin.site.register(Contact)