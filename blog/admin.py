from django.contrib import admin

from .models import Blog, Single, Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'approved')

class SingleInline(admin.TabularInline):
    model = Single
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title_text']}),
        (None, {'fields': ['image']}),
        (None, {'fields': ['head_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('title_text', 'pub_date', 'was_published_recently')
    inlines = [SingleInline]
    list_filter = ['pub_date']



admin.site.register(Blog, BlogAdmin)
admin.site.register(Single)
admin.site.register(Comment, CommentAdmin)