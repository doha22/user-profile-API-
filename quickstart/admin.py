from django.contrib import admin
from .import models
# Register your models here.


## chose which model will the admin can use##
admin.site.register(models.UserProfile)