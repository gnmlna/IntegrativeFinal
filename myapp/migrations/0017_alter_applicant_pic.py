# Generated by Django 4.2.1 on 2023-05-15 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_applicant_pic_alter_applicant_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='myapp/applicant_pics/'),
        ),
    ]
