################# Libs #################
from django.contrib import admin
from . import models
from django.db.models.aggregates import Count
########################################

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):

    pass


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass