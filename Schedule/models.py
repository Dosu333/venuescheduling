from django.db import models
from accounts.models import User

# Create your models here.

class Timetable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    Name = models.CharField(max_length=50, default='courses')
    Date = models.DateField(blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    VENUE_CHOICES = [
            ('PY102', "PY102"),
            ('ZIBAMBWE',"ZIBAMBWE"),
            ('AJOSE', "AJOSE"),
            ('1000SLT',"1000SLT"),
            ('ADMIN EXT RM A',"ADMIN EXT RM A"),
            ('AUD1', "AUD1"),
            ('AUD2',"AUD2"),
            ('ODLT1',"ODLT1"),
            ('ODLT2',"ODLT2"),
            ('PY130',"PY130"),
            ('PY238', "PY238"),
            ('BOOA',"BOOA"),
            ('BOOB',"BOOB"),
            ('BOOC', "BOOC"),
        ]
    Venue = models.CharField(max_length=50, choices=VENUE_CHOICES)

    PURPOSE_CHOICES =[
        ('Lecture', "Lecture"),
        ('Defence',"Defence"),
        ('Meeting', "Meeting"),
        ('Seminar', "Seminar"),
        ('Test', "Test"),
        ('Exam', "Exam"),
    ]
    purpose = models.CharField(max_length=7, choices=PURPOSE_CHOICES, null=False)

    DAYS_CHOICES = [
        ('0',"Monday"),
        ('1', "Tuesday"),
        ('2',"Wednesday"),
        ('3', "Thursday"),
        ('4', "Friday"),
        ('5', "Saturday"),
    ]
    days = models.CharField(max_length=10, choices=DAYS_CHOICES, blank=True, null=True)

    STATUS_CHOICES = [
        ('TEMPORARY',"Temporary"),
        ('PERMANENT',"Permanent"),
    ]
    allocation_status = models.CharField(max_length=10, choices=STATUS_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.Venue
