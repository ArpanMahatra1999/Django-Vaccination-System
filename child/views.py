from django.shortcuts import reverse

from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from child.models import Child
from child.forms import CreateChildForm, UpdateChildForm

from vaccine.models import Vaccine, Dose, Schedule


# Create your views here.
@method_decorator(login_required, name='dispatch')
class CreateChildView(CreateView):
    form_class = CreateChildForm
    template_name = 'child/create.html'

    def form_valid(self, form):
        child = form.save(commit=False)
        child.parent = self.request.user
        return super(CreateChildView, self).form_valid(form)

    def get_success_url(self):
        return reverse('child:list-child')


@method_decorator(login_required, name='dispatch')
class ListChildView(ListView):
    model = Child
    template_name = 'child/list.html'
    context_object_name = 'children'


@method_decorator(login_required, name='dispatch')
class UpdateChildView(UpdateView):
    model = Child
    form_class = UpdateChildForm
    template_name = 'child/update.html'
    context_object_name = 'child'

    def get_success_url(self):
        return reverse('child:list-child')


@method_decorator(login_required, name='dispatch')
class DeleteChildView(DeleteView):
    model = Child
    template_name = 'child/delete.html'
    context_object_name = 'child'

    def get_success_url(self):
        return reverse('child:list-child')


@method_decorator(login_required, name='dispatch')
class DetailChildView(DetailView):
    model = Child
    template_name = 'child/detail.html'
    context_object_name = 'child'

    def get_context_data(self, **kwargs):
        context = super(DetailChildView, self).get_context_data(**kwargs)
        schedules = Schedule.objects.filter(child=self.object)
        vaccines = []
        for vaccine in Vaccine.objects.all():
            for schedule in schedules:
                if vaccine == schedule.dose.vaccine:
                    vaccines.append(vaccine)
        vaccines = list(set(vaccines))
        context['schedules'] = schedules
        context['vaccines']= vaccines
        return context