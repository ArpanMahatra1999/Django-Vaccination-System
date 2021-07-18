from django.shortcuts import reverse

from django.views.generic import ListView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from datetime import date

from vaccine.models import Schedule
from vaccine.forms import UpdateScheduleForm


# Create your views here.
@method_decorator(login_required, name='dispatch')
class ListScheduleView(ListView):
    model = Schedule
    template_name = 'schedule/list.html'
    context_object_name = 'schedules'


@method_decorator(login_required, name='dispatch')
class VaccinatedListScheduleView(ListView):
    model = Schedule
    template_name = 'schedule/vaccinated_list.html'
    context_object_name = 'schedules'


@method_decorator(login_required, name='dispatch')
class UnvaccinatedListScheduleView(ListView):
    model = Schedule
    template_name = 'schedule/unvaccinated_list.html'
    context_object_name = 'schedules'


@method_decorator(login_required, name='dispatch')
class UpdateScheduleView(UpdateView):
    model = Schedule
    form_class = UpdateScheduleForm
    template_name = 'schedule/update.html'
    context_object_name = 'schedule'

    def form_valid(self, form):
        schedule = form.save(commit=False)
        if schedule.vaccinated:
            schedule.date_of_vaccination = date.today()
        return super(UpdateScheduleView, self).form_valid(form)

    def get_success_url(self):
        return reverse('vaccine:vaccinated-list-schedule')