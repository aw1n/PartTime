from django.db import models
from django.contrib.auth.models import User, UserManager

class Company(models.Model):
    user = models.OneToOneField(User)
    user_timezone = models.CharField(max_length=50, default='Europe/London')
    
    company_name        = models.CharField(max_length=100)
    company_web         = models.CharField(max_length=100, null=True, blank=True)
    company_mail        = models.EmailField(null=True, blank=True)
    company_description = models.TextField(max_length=2000, null=True, blank=True)


    
    
