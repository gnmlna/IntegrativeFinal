# Generated by Django 4.2.1 on 2023-05-15 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_remove_student_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Applicant',
        ),
    ]
