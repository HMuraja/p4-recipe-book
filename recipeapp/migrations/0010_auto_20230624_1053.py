# Generated by Django 3.2.19 on 2023-06-24 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0009_alter_recipe_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='cooking_time',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='region',
            field=models.CharField(choices=[('Abruzzo', 'Abruzzo'), ('Aosta valley', 'Aosta valley'), ('Apulia', 'Apulia'), ('Basilicata', 'Basilicata'), ('Calabria', 'Calabria'), ('Campania', 'Calabria'), ('Emilia-Romagna', 'Emilia-Romagna'), ('Friuli-Venezia Giulia', 'Friuli-Venezia Giulia'), ('Lazio', 'Lazio'), ('Liguria', 'Liguria'), ('Lombardy', 'Lombardy'), ('Marche', 'Marche'), ('Molise', 'Molise'), ('Piedmont', 'Piedmont'), ('Sardinia', 'Sardinia'), ('Sicily', 'Sicily'), ('Trentino-South Tyrol', 'Trentino-South Tyrol'), ('Tuscany', 'Tuscany'), ('Umbria', 'Umbria'), ('Veneto', 'Veneto'), ('Unknown', 'Region Unknown'), ('None', 'No Specific Region')], default='None', max_length=80),
        ),
    ]