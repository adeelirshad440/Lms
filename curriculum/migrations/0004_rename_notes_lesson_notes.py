# Generated by Django 3.2.4 on 2021-06-26 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0003_rename_standard_lesson_standard'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='notes',
            new_name='Notes',
        ),
    ]
