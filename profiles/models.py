from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PilotProfile(models.Model):

    CREW_BASE_CHOICES = [
        ("EDDF", "Frankfurt"),
        ("KMIA", "Miami"),
        ("KORD", "Chicago O'Hare"),
        ("PANC", "Anchorage"),
        ("RJAA", "Tokyo Narita"),
    ]

    AIRCRAFT_TYPE_CHOICES = [
        ("B737", "737-700 BDSF"),
        ("B738", "737-800 BDSF"),
        ("B75F", "757-200F"),
        ("B76F", "767-300F"),
        ("B77F", "777-200F"),
        ("B74F", "747-400F"),
        ("B78F", "747-8F"),
    ]

    crew_base = models.CharField(
        "Assigned crew base",
        max_length=30,
        help_text="Your assigned crew base",
        choices=CREW_BASE_CHOICES,
    )
    aircraft_types = models.CharField(
        "Assigned aircraft type",
        max_length=50,
        help_text="Your last name",
        choices=AIRCRAFT_TYPE_CHOICES,
    )
    total_hours = (models.DecimalField("Total hours"),)
    B737_hours = (models.DecimalField("737-700 BDSF"),)
    B738_hours = (models.DecimalField("737 737-800 BDSF"),)
    # B75F_hours = models.DecimalField("757-200F"),
    # B76F_hours = models.DecimalField("767-300F"),
    # B77F_hours = models.DecimalField("777-200F"),
    B74F_hours = (models.DecimalField("747-400F"),)
    B78F_hours = (models.DecimalField("747-8F"),)
