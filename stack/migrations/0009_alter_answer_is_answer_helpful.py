# Generated by Django 4.0.3 on 2022-03-13 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0008_rename_is_helpful_answer_is_answer_helpful'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='is_answer_helpful',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
