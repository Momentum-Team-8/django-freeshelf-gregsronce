# Generated by Django 3.2.4 on 2021-06-23 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(related_name='books', to='books.Category'),
        ),
    ]
