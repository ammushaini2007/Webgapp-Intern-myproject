from django.contrib import admin
from .models import Forms


# Register your models here.
class FormsAdmin(admin.ModelAdmin):
    list_display=('name','number','dob','mobile','email','password','city','address','father','department','Gender')
admin.site.register(Forms,FormsAdmin)
