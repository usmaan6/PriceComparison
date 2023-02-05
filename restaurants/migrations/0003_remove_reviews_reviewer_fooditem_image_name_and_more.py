# Generated by Django 4.1.5 on 2023-02-05 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurant_image_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='Reviewer',
        ),
        migrations.AddField(
            model_name='fooditem',
            name='image_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='type',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]
