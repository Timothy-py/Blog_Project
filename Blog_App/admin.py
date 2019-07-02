from django.contrib import admin
from Blog_App.models import Post,Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    fields = ['title','text','author', 'image', 'create_date','published_date']
    search_fields = ['author__username__icontains']


admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
# admin.site.register(Reply)
