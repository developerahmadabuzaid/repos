from django.db import models

# Create your models here.

class NewsArticle(models.Model):
    title = models.CharField(max_length=200, verbose_name="عناون الخبر")
    date = models.DateField(verbose_name="تاريخ الخبر")
    details = models.TextField(verbose_name="التفاصيل")
    image = models.ImageField(upload_to="news_images/", verbose_name="صورة", null=True, blank=True)

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    name = models.CharField(max_length=100, verbose_name="الاسم")
    job_title = models.CharField(max_length=100, verbose_name="الوظيفة الحالية")
    birth_year = models.IntegerField(verbose_name="تاريخ الولادة")
    bio = models.TextField(verbose_name="السيرة الذاتية")
    image = models.ImageField(upload_to="profile_images/", verbose_name="الصورة", null=True, blank=True)

    def __str__(self):
        return self.name
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="الاسم")
    email = models.EmailField(verbose_name="البريد الالكتروني")
    message = models.TextField(verbose_name="الرسالة")

    def __str__(self):
        return self.name