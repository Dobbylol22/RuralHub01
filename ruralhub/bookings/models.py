from django.db import models
from django.conf import settings


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()

    def __str__(self):
        return f"Booking for {self.user.username} on {self.booking_date} at {self.booking_time}"
