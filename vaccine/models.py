from django.db import models

import datetime

# Create your models here.
class Vaccine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    route = models.TextField(blank=True, null=True)
    site = models.TextField(blank=True, null=True)
    side_effects = models.TextField(blank=True, null=True)
    before_care = models.TextField(blank=True, null=True)
    after_care = models.TextField(blank=True, null=True)
    protect_against = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Dose(models.Model):
    UNITS = (
        ('ml', 'ml'),
        ('drop', 'drop')
    )
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=255, choices=UNITS)
    first_day_from_birth = models.PositiveIntegerField()
    last_day_from_birth = models.PositiveIntegerField()
    booster = models.BooleanField(default=False)
    compulsory_after_birth = models.BooleanField(default=False)

    def __str__(self):
        return str(self.vaccine) + " dose " + str(self.number)


class Schedule(models.Model):
    dose = models.ForeignKey(Dose, on_delete=models.CASCADE)
    child = models.ForeignKey('child.Child', on_delete=models.CASCADE)
    date_of_vaccination = models.DateField(blank=True, null=True)
    vaccinated = models.BooleanField(default=False)

    def get_status(self):
        if datetime.date.today() < self.child.date_of_birth + datetime.timedelta(days=self.dose.first_day_from_birth):
            time_delta_value = self.child.date_of_birth + datetime.timedelta(days=self.dose.first_day_from_birth) - datetime.date.today()
            days_remaining = time_delta_value.days
            return ["Yellow", days_remaining]
        elif datetime.date.today() >= self.child.date_of_birth + datetime.timedelta(days=self.dose.first_day_from_birth) and datetime.date.today() < self.child.date_of_birth + datetime.timedelta(days=self.dose.last_day_from_birth):
            time_delta_value = self.child.date_of_birth + datetime.timedelta(days=self.dose.last_day_from_birth) - datetime.date.today()
            days_remaining = time_delta_value.days
            return ["Green", days_remaining]
        else:
            time_delta_value = datetime.date.today() - (self.child.date_of_birth + datetime.timedelta(days=self.dose.last_day_from_birth))
            days_passed = time_delta_value.days
            return ["Red", days_passed]


    def __str__(self):
        return str(self.child) + "'s vaccination for " + str(self.dose)
