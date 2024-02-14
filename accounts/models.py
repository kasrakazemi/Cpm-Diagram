################# Libs #################
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
########################################

class User(AbstractUser):
    email = models.EmailField(unique=True)
    

class Profile(models.Model):
    English = 'En'
    Spanish = 'Es'
    French = 'Fr'
    
    LanguageChoices = [
                       (English,'English'),
                       (Spanish,'Spanish'),
                       (French,'French')
                       ]

    name = models.CharField(max_length = 255)
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    family_name = models.CharField(max_length = 255)
    birth_date = models.DateField(null=True)
    phone = PhoneNumberField(unique = True, blank=True, null=True)
    language = models.CharField(max_length=3,choices= LanguageChoices,default = English)

    # change default object names in admin pannel
    def __str__(self):
        return self.name
    
    