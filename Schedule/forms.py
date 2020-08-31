from django import forms
from .models import Timetable
from datetime import time,date
import datetime

class ScheduleForm(forms.ModelForm):
    Date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    start_time = forms.TimeField(help_text='Use 24hrs clock. Time must be within working hours 7:00 - 19:00', widget=forms.TimeInput(attrs={'placeholder':'HH:MM:SS'}))
    end_time = forms.TimeField(help_text='Use 24hrs clock. Time must be within working hours 7:00 - 19:00', widget=forms.TimeInput(attrs={'placeholder':'HH:MM:SS'}))
    PURPOSE_CHOICES =[
        ('Lecture', "Lecture"),
        ('Defence',"Defence"),
        ('Meeting', "Meeting"),
        ('Seminar', "Seminar"),
        ('Test', "Test"),
    ]
    purpose = forms.ChoiceField(choices=PURPOSE_CHOICES)
    class Meta:
        model = Timetable
        fields = ('Name',)

    def clean(self):
        start_work_time = time(7,00,00)
        end_work_time = time(19,00,00)
        cleaned_data = super().clean()
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")
        Date = cleaned_data.get("Date")
        if start_time and end_time:
            if start_time < start_work_time or start_time > end_work_time  or end_time < start_work_time or end_time > end_work_time  :
                raise forms.ValidationError("Times must be within working hours")
            if start_time > end_time:
                raise forms.ValidationError("You can't use a venue for that long! 'End time' must be greater than 'Start time' ")
        if Date:

            if date.fromisoformat(str(Date))  != Date:
                raise forms.ValidationError("Date must be in YYYY-MM-DD format")

            if date.today() > Date:
                raise forms.ValidationError("You can't schedule a venue in the past. Change Date")
