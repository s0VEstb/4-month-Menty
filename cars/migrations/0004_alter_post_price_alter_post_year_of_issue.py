# Generated by Django 5.0.4 on 2024-04-14 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_remove_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='year_of_issue',
            field=models.DateField(),
        ),
    ]