# Generated by Django 3.2.19 on 2023-06-24 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0007_alter_recipe_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='region',
            field=models.CharField(choices=[('Abruzzo', 'Abruzzo'), ('Aosta valley', 'Aosta valley'), ('Apulia', 'Apulia'), ('Basilicata', 'Basilicata'), ('Calabria', 'Calabria'), ('Campania', 'Calabria'), ('Emilia-Romagna', 'Emilia-Romagna'), ('Friuli-Venezia Giulia', 'Friuli-Venezia Giulia'), ('Lazio', 'Lazio'), ('Liguria', 'Liguria'), ('Lombardy', 'Lombardy'), ('Marche', 'Marche'), ('Molise', 'Molise'), ('Piedmont', 'Piedmont'), ('Sardinia', 'Sardinia'), ('Sicily', 'Sicily'), ('Trentino-South Tyrol', 'Trentino-South Tyrol'), ('Tuscany', 'Tuscany'), ('Umbria', 'Umbria'), ('Veneto', 'Veneto'), ('Unknown', 'Unknown'), ('None', 'None')], max_length=80),
        ),
    ]
