from django.db import models

from django.contrib.auth.models import User

from vaccine.models import Dose, Schedule

# Create your models here.
class Child(models.Model):

    GENDERS = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDERS)
    photo = models.ImageField(null=True, blank=True, upload_to='images/child/')
    date_of_birth = models.DateField()
    place_of_birth = models.TextField()
    place_of_vaccination = models.TextField()
    parent = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            for dose in Dose.objects.all():
                if dose.compulsory_after_birth == True:
                    Schedule.objects.create(
                        dose=dose,
                        child=self,
                    )

    def __str__(self):
        return str(self.name)


