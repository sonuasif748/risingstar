# Generated by Django 3.2.4 on 2021-08-03 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0005_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_categories',
            name='discription',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='add_categories',
            name='movie_link',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='add_categories',
            name='status',
            field=models.BooleanField(default=0),
        ),
    ]
