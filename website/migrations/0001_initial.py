from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("slug", models.SlugField(unique=True)),
                ("short_description", models.CharField(max_length=240)),
                ("description", models.TextField()),
                ("is_featured", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("sort_order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["sort_order", "name"]},
        ),
        migrations.CreateModel(
            name="PricingPlan",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=80)),
                ("subtitle", models.CharField(blank=True, max_length=180)),
                ("price_label", models.CharField(default="Contact", max_length=80)),
                ("features", models.TextField(help_text="Enter one feature per line.")),
                ("is_featured", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("sort_order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["sort_order", "name"]},
        ),
        migrations.CreateModel(
            name="DemoRequest",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("company", models.CharField(max_length=160)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=40)),
                ("company_type", models.CharField(choices=[("engineering","Engineering"),("mep","MEP"),("solar","Solar"),("construction","Construction"),("technical","Technical Services"),("other","Other")], max_length=30)),
                ("users", models.CharField(choices=[("1-5","1–5"),("6-15","6–15"),("16-50","16–50"),("50+","50+")], max_length=20)),
                ("requirements", models.TextField(blank=True)),
                ("status", models.CharField(choices=[("new","New"),("contacted","Contacted"),("scheduled","Demo Scheduled"),("closed","Closed")], default="new", max_length=20)),
                ("admin_notes", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.CreateModel(
            name="ContactEnquiry",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("company", models.CharField(blank=True, max_length=160)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(blank=True, max_length=40)),
                ("subject", models.CharField(max_length=180)),
                ("message", models.TextField()),
                ("status", models.CharField(choices=[("new","New"),("contacted","Contacted"),("closed","Closed")], default="new", max_length=20)),
                ("admin_notes", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
