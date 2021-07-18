from django.shortcuts import reverse

from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from application.forms import CreateApplicationForm

from child.models import Child

# Create your views here.
@method_decorator(login_required, name='dispatch')
class CreateApplicationView(CreateView):
    form_class = CreateApplicationForm
    template_name = 'application/create.html'

    def form_valid(self, form):
        application = form.save(commit=False)
        application.child = Child.objects.get(id=self.kwargs['pkc'])
        return super(CreateApplicationView, self).form_valid(form)

    def get_success_url(self):
        return reverse('child:list-child')