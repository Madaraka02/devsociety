# Generated by Django 4.0.3 on 2022-03-10 20:31

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('slug', models.SlugField(null=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='blog_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor.fields.RichTextField(null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.blog')),
            ],
        ),
    ]