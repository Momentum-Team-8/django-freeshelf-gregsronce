# Generated by Django 3.2.4 on 2021-06-23 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_cover_art'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cover_art',
        ),
    ]
