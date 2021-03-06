# Generated by Django 4.0.4 on 2022-05-31 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogpost_featured_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=254)),
                ('comment', models.TextField(max_length=5000)),
                ('comment_initiated_on', models.DateTimeField(auto_now_add=True)),
                ('comment_updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=False)),
                ('blogpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blogpost')),
            ],
            options={
                'ordering': ('-comment_initiated_on',),
            },
        ),
    ]
