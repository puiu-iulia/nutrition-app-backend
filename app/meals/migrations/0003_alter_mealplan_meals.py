# Generated by Django 4.0.6 on 2022-07-15 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_mealplan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealplan',
            name='meals',
            field=models.ManyToManyField(blank=True, null=True, to='meals.meal'),
        ),
    ]
