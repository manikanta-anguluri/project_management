from django.contrib import admin
from register_app.models import Company,UserProfile
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Company)    
