# Generated by Django 3.2.19 on 2023-06-24 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0011_alter_recipe_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]
