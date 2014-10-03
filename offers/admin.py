from django.contrib import admin
from offers.models import Company

class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
                 ('User',        {'fields':['user', 'user_timezone']}),
                 ('Company',           {'fields':['company_name', 'company_web', 'company_description']}),
                 ]

admin.site.register(Company, CompanyAdmin)
