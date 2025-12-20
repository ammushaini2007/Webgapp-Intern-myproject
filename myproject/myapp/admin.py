from django.contrib import admin
from .models import Forms


# Register your models here.
class FormsAdmin(admin.ModelAdmin):
    list_display=('name','number','dob')
admin.site.register(Forms,FormsAdmin)
