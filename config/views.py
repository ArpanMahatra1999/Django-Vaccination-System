from django.shortcuts import render

from django.views.generic import TemplateView
import smtplib

from vaccine.models import Vaccine, Schedule

from config.settings import EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD


def notification(request):
    server = smtplib.SMTP_SSL(EMAIL_HOST, 465)
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    unvaccinated_schedules = Schedule.objects.filter(vaccinated=False)
    for schedule in unvaccinated_schedules:
        if schedule.get_status()[0] == 'Yellow':
            server.sendmail(EMAIL_HOST_USER, schedule.child.parent.email, f'Subject:' + str(schedule) + ' notification \n\n' + str(schedule.get_status()[1]) + ' days remaining till first day of vaccination')
        elif schedule.get_status()[0] == 'Green':
            server.sendmail(EMAIL_HOST_USER, schedule.child.parent.email, f'Subject:' + str(schedule) + ' notification \n\n' + str(schedule.get_status()[1]) + ' days remaining till last day of vaccination')
        else:
            server.sendmail(EMAIL_HOST_USER, schedule.child.parent.email, f'Subject:' + str(schedule) + ' notification \n\n' + str(schedule.get_status()[1]) + ' days passed after last day of vaccination')
    server.quit()
    return render(request, 'notification.html')


class HomeView(TemplateView):
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vaccines'] = Vaccine.objects.all()
        return context