# Generated by Django 3.2.4 on 2021-06-04 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_meal_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='preperation_tim',
            new_name='preperation_time',
        ),
    ]