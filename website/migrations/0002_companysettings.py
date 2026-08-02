from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompanySettings",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("company_name", models.CharField(default="AR Solutions", max_length=160)),
                ("tagline", models.CharField(blank=True, default="Smart Solutions. Stronger Businesses.", max_length=240)),
                ("email", models.EmailField(blank=True, default="sales@arsolutions.com", max_length=254)),
                ("phone", models.CharField(blank=True, max_length=40)),
                ("whatsapp", models.CharField(blank=True, help_text="Enter country code and number only, for example 971500000000.", max_length=40)),
                ("website", models.URLField(blank=True)),
                ("address", models.TextField(blank=True)),
                ("google_maps_url", models.URLField(blank=True)),
                ("working_hours", models.CharField(blank=True, default="Monday–Saturday, 9:00 AM–6:00 PM", max_length=180)),
                ("facebook_url", models.URLField(blank=True)),
                ("instagram_url", models.URLField(blank=True)),
                ("linkedin_url", models.URLField(blank=True)),
                ("youtube_url", models.URLField(blank=True)),
                ("copyright_text", models.CharField(blank=True, default="AR Solutions. All rights reserved.", max_length=240)),
            ],
            options={
                "verbose_name": "Company Settings",
                "verbose_name_plural": "Company Settings",
            },
        ),
    ]
