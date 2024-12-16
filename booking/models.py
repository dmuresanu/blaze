from django.db import models

# Booking model with both fields
class Booking(models.Model):
    # Fields from the first Booking model
        name = models.CharField(max_length=100)
        email = models.EmailField()
        date = models.DateField()

        def __str__(self):
            return f"{self.name} - {self.date}"

class Booking(models.Model):
    # Existing fields...
    TIME_SLOTS = [
        ('morning', 'Morning (9 AM - 12 PM)'),
        ('afternoon', 'Afternoon (12 PM - 3 PM)'),
        ('evening', 'Evening (6 PM - 9 PM)'),
    ]
    time_slot = models.CharField(max_length=10, choices=TIME_SLOTS, default='morning')

