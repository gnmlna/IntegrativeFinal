# Generated by Django 4.2.1 on 2023-05-20 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_remove_applicant_pic_applicant_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='childNumber',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='civilStatus',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='job',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
