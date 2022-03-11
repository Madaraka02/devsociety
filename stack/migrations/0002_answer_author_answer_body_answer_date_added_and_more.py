# Generated by Django 4.0.3 on 2022-03-10 19:27

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='body',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stack.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
