from django.contrib import admin
from .models import post,comment

class postAdmin(admin.ModelAdmin):
    pass
    
class commentAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(post, postAdmin)

admin.site.register(comment, commentAdmin)
