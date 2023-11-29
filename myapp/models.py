from django.db import models


class Applicant(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    TIME_CHOICES = (
        ('8:00AM', '8:00AM'),
        ('9:00AM', '9:00AM'),
        ('10:00AM', '10:00AM'),
        ('11:00AM', '11:00AM'),
        ('12:00PM', '12:00PM'),
        ('1:00PM', '1:00PM'),
        ('2:00PM', '2:00PM'),
        ('3:00PM', '3:00PM'),
        ('4:00PM', '4:00PM'),
        ('5:00PM', '5:00PM'),
    )

    CIVIL_STATUS = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Separated', 'Separated'),
        ('Widowed', 'Widowed'),
        ('Never Married', 'Never Married'),

        
    )



    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    job = models.CharField(max_length=250, null=True)
    income = models.CharField(max_length=200)
    childNumber = models.CharField(max_length=200, null=True)
    civilStatus = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES)
    appdate = models.CharField(max_length=20)
    apptime = models.CharField(max_length=20, choices=TIME_CHOICES)
    image = models.ImageField(upload_to='applicant_pics/covers', null=True, blank=True)
    status = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


# Create your models here.
