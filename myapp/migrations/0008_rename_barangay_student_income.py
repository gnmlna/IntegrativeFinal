# Generated by Django 4.1.7 on 2023-05-02 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_student_region_alter_student_apptime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='barangay',
            new_name='income',
        ),
    ]
