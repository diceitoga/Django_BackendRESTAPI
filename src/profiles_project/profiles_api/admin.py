from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
'''
In the django.contrib, there is admin module that we importedself.
In that module is a site module which has a prebuilt function called
register, in which you pass the model you want to registerself.
In this particular case, it is models==models object and UserProfile,
which you defined in models.py
'''
