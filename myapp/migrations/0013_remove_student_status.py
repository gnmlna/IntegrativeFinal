# Generated by Django 4.1.7 on 2023-05-02 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_student_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='status',
        ),
    ]
