# Generated by Django 5.0.6 on 2024-06-10 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_books_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='rating',
        ),
    ]
