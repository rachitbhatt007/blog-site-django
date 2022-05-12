from django.contrib import admin
from .models import Post, Author, Tag,Comment

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" :("title",)}
    list_filter = ("author","tag","date")
    list_display = ("title","date","author")

class AuthorAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email")    
# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
