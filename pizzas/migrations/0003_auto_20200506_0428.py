# Generated by Django 3.0.6 on 2020-05-06 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_topping'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topping',
            old_name='name',
            new_name='text',
        ),
    ]
