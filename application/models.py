from django.db import models

from child.models import Child
from vaccine.models import Vaccine, Dose, Schedule


# Create your models here.
class Application(models.Model):
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date_of_application = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            for dose in Dose.objects.all():
                if dose.vaccine == self.vaccine:
                    Schedule.objects.create(
                        dose=dose,
                        child=self.child,
                    )

    def __str__(self):
        return str(self.vaccine) + " for " + str(self.child)