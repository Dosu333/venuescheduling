from django.urls import path
from django.shortcuts import reverse
from . views import ScheduleView, AllocatedVenueView, delTable
from . import views

app_name = 'Schedule'

urlpatterns = [
    path('schedule/', ScheduleView.as_view(), name = 'schedule' ),
    path('success/<venue>/', views.SuccessView, name = 'successful' ),
    path('allocation/', AllocatedVenueView.as_view(), name='allocation' ),
    path('<pk>/delete', delTable.as_view(), name = 'delete'),
]
