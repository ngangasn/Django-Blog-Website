# Generated by Django 4.0.4 on 2022-05-31 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_author_alter_blogpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/images'),
        ),
    ]
