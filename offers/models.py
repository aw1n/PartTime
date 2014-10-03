from django.db import models
from django.contrib.auth.models import User, UserManager


class CompanyManager(models.Manager):
     
    def create_company(self, params, activation_key, key_expires):

        u = User.objects.create_user(params['username'],
                                     email=params['email'],
                                     password=params['password'],
                                     first_name=params['user_firstname'],
                                     last_name=params['user_lastname']
                                     )
        u.set_password(u.password)
        u.save()
            
        c = self.create(user=u, 
                    company_name=params['company_name'],
                    company_web=params['company_web'],
                    company_description=params['company_description'],
                    activation_key = activation_key, 
                    key_expires = key_expires)
        return c


class Company(models.Model):
    user                = models.OneToOneField(User)
    user_timezone       = models.CharField(max_length=50, default='Europe/London')
    
    company_name        = models.CharField(max_length=100)
    company_web         = models.CharField(max_length=100, null=True, blank=True)
    company_description = models.TextField(max_length=2000, null=True, blank=True)
    
    activation_key      = models.CharField(max_length=40, null=True)
    key_expires         = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.company_name
    
    objects = CompanyManager()


User.profile = property(lambda u: Company.objects.get_or_create(user=u)[0])