# Generated by Django 4.1 on 2022-12-21 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0002_alter_family_dni'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='family',
            name='birthdate',
        ),
    ]
