# Generated by Django 3.2.4 on 2021-06-26 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0002_alter_lesson_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='standard',
            new_name='Standard',
        ),
    ]
