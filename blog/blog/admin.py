from django.contrib import admin
from blog.models import Category, Comment, Post, Author # import the models to register on the admin page
from django_summernote.admin import SummernoteModelAdmin

class CategoryAdmin(admin.ModelAdmin):
    pass


class PostAdmin(SummernoteModelAdmin):
    # fields = ['title', 'body', 'author', 'categories']
    # search_fields = ['author__name']
    #summernote_fields = ('body',)
    readonly_fields = ('body_as_summernote',)

class AuthorAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

# register models with the admin classes
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)
