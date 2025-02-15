from django.contrib import admin
from .models import NewsArticle,Profile,Contact

# Register your models here.
admin.site.register(NewsArticle)
admin.site.register(Profile)
admin.site.register(Contact)

class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'details')
    search_fields = ('title', 'details')
    list_filter = ('date',)
    
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title', 'birth_year')
    search_fields = ('name', 'job_title')
    list_filter = ('birth_year',)
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')
    list_filter = ('email',)