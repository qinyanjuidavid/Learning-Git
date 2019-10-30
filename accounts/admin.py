from django.contrib import admin
from accounts.models import User
from accounts.forms import customuserchangeform, customusercreationform




class UserAdmin(admin.ModelAdmin):
    search_fields=['email']
    form=customuserchangeform
    add_form=customusercreationform
    model=User
    list_display=['email']
    #class Meta:
    #    model=User
admin.site.register(User,UserAdmin)
