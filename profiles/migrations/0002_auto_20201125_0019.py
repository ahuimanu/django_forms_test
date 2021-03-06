# Generated by Django 3.1.3 on 2020-11-25 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PilotProfile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "crew_base",
                    models.CharField(
                        choices=[
                            ("EDDF", "Frankfurt"),
                            ("KMIA", "Miami"),
                            ("KORD", "Chicago O'Hare"),
                            ("PANC", "Anchorage"),
                            ("RJAA", "Tokyo Narita"),
                        ],
                        help_text="Your assigned crew base",
                        max_length=30,
                        verbose_name="Assigned crew base",
                    ),
                ),
                (
                    "aircraft_types",
                    models.CharField(
                        choices=[
                            ("B737", "737-700 BDSF"),
                            ("B738", "737-800 BDSF"),
                            ("B75F", "757-200F"),
                            ("B76F", "767-300F"),
                            ("B77F", "777-200F"),
                            ("B74F", "747-400F"),
                            ("B78F", "747-8F"),
                        ],
                        help_text="Your last name",
                        max_length=50,
                        verbose_name="Assigned aircraft type",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(name="Profile",),
    ]
