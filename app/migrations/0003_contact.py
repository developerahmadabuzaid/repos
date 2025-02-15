# Generated by Django 5.1.6 on 2025-02-15 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='الاسم')),
                ('email', models.EmailField(max_length=254, verbose_name='البريد الالكتروني')),
                ('message', models.TextField(verbose_name='الرسالة')),
            ],
        ),
    ]
