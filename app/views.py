from django.shortcuts import render
from .models import NewsArticle,Profile,Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')

def news_list(request):
    articles = NewsArticle.objects.all().order_by('-date')
    return render(request, 'news_list.html', {'articles': articles})

def about_view(request):
    profile = Profile.objects.first()  # احصل على أول ملف تعريف (يمكن تعديل هذا الاستعلام)
    return render(request, 'about.html', {'profile': profile})

def contact_view(request):
    contact = Contact.objects.first()
    return render(request, 'contact_view.html', {'contact': contact})