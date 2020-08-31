from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import ScheduleForm
from .models import Timetable
from datetime import date, time
import datetime
# Create your views here.

def is_between(time, time_range):
    if time_range[1] < time_range[0]:
        return time > time_range[0] or time < time_range[1]
    return time_range[0] < time < time_range[1]

def getDayOfWeek(ojo):
    if ojo != None:
        str_date = str(ojo)
        format_date = date.fromisoformat(str_date)
        return str(format_date.weekday())





class ScheduleView(FormView):
    form_class = ScheduleForm
    template_name = 'Schedule/Schedule.html'
    success_url = 'Schedule/available_venues.html'
    for objects in Timetable.objects.all():
        if objects.Date != None:
            if date.today() > objects.Date:
                objects.delete()
            elif date.today() == objects.Date and datetime.datetime.now().time() > end_time:
                objects.delete()

    def form_valid(self,form):
        request = self.request
        if not form.errors:
            ven_show = []
            ven_no = []
            unique = []
            ven_not_day = []
            ven_day = []
            displace = []
            final =[]

            name = form.cleaned_data['Name']
            date = form.cleaned_data['Date']
            purpose = form.cleaned_data['purpose']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            context = {'form':form}
            day = getDayOfWeek(date)

            s_time=str(start_time)
            e_time = str(end_time)
            strDate = str(date)


            request.session['Name'] = name
            request.session['strDate'] = strDate
            request.session['purpose'] = purpose
            request.session['s_time'] = s_time
            request.session['e_time'] = e_time



            for items in Timetable.objects.all():
                if day == items.days or date == items.Date:
                     ven_day.append(items)
                else:
                    ven_not_day.append(items)

            for items in ven_day:
                if items.start_time != start_time:
                    ven_show.append(items)

                    # elif purpose == "Lecture" and items.purpose != "Lecture" and items.purpose != "Meeting" and date.today().weekday() + 3 <= int(day):
                    #     ven_show.append(items)
                    # elif purpose != "Meeting" and items.purpose == "Meeting" and date.today().weekday() + 2 <= int(day):
                    #     ven_show.append(items)

                else:
                    ven_no.append(items)

            for items in ven_show:
                if is_between(start_time, (items.start_time, items.end_time)) or is_between(items.start_time,(start_time,end_time)):
                    ven_no.append(items)

            for obj in ven_show:
                for ven in ven_no:
                    if obj.Venue == ven.Venue:
                        displace.append(obj)

            for obj in ven_not_day:
                for ven in ven_day:
                    if obj.Venue == ven.Venue:
                        unique.append(obj)

            for objects in displace:
                ven_show.remove(objects)

            for items in ven_not_day:
                if items not in unique:
                    ven_show.append(items)

            for items in ven_show:
                final.append(items.Venue)

            final_set = set(final)
            final_list = list(final_set)

            args = {'ven_show':final_list, 'ven_day':ven_day, 'ven_no':ven_no}
            return render(request, self.success_url, args)
        else:
            print("Error")
            return render(request, self.template_name, context)





def SuccessView(request, venue):
    name = request.session['Name']
    strDate = request.session['strDate']
    purpose = request.session['purpose']
    startObject = request.session['s_time']
    endObject = request.session['e_time']
    user_id = request.user

    new = Timetable(user=user_id, Date=strDate, purpose=purpose, start_time=startObject, end_time=endObject, Name=name, Venue=venue)
    new.save()

    messages.success(request, "Your have scheduled for %s successfully" %venue)
    return HttpResponseRedirect('/Schedule/allocation/')


class AllocatedVenueView(TemplateView):
    template_name = 'Schedule/allocated_venues.html'

    def get(self, request):
        users_allocation = Timetable.objects.filter(user=request.user)

        return render(request, self.template_name, {'users_allocation':users_allocation})


def delete(request, id):
    ItemToDelete = get_object_or_404(Timetable,pk=id)
    venue = ItemToDelete.Venue
    date = str(ItemToDelete.Date)
    purpose = ItemToDelete.purpose
    ItemToDelete.delete()

    messages.success(request, "Your have successfully cancelled your schedule for a %s at %s on %s" %(purpose, venue, date))

    return HttpResponseRedirect('/Schedule/allocation/')

def ii():
