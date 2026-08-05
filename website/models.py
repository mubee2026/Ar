from django.core.exceptions import ValidationError
from django.db import models
from cloudinary.models import CloudinaryField

class Product(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=240)
    description = models.TextField()
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name


class PricingPlan(models.Model):
    name = models.CharField(max_length=80)
    subtitle = models.CharField(max_length=180, blank=True)
    price_label = models.CharField(max_length=80, default="Contact")
    features = models.TextField(help_text="Enter one feature per line.")
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "name"]

    def feature_list(self):
        return [line.strip() for line in self.features.splitlines() if line.strip()]

    def __str__(self):
        return self.name


class DemoRequest(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("scheduled", "Demo Scheduled"),
        ("closed", "Closed"),
    ]
    COMPANY_TYPE_CHOICES = [
        ("engineering", "Engineering"),
        ("mep", "MEP"),
        ("solar", "Solar"),
        ("construction", "Construction"),
        ("technical", "Technical Services"),
        ("other", "Other"),
    ]
    USER_RANGE_CHOICES = [
        ("1-5", "1–5"),
        ("6-15", "6–15"),
        ("16-50", "16–50"),
        ("50+", "50+"),
    ]

    name = models.CharField(max_length=120)
    company = models.CharField(max_length=160)
    email = models.EmailField()
    phone = models.CharField(max_length=40)
    company_type = models.CharField(max_length=30, choices=COMPANY_TYPE_CHOICES)
    users = models.CharField(max_length=20, choices=USER_RANGE_CHOICES)
    requirements = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    admin_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.company} - {self.name}"


class ContactEnquiry(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("closed", "Closed"),
    ]
    name = models.CharField(max_length=120)
    company = models.CharField(max_length=160, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    subject = models.CharField(max_length=180)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    admin_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.subject} - {self.name}"


class CompanySettings(models.Model):
    company_name = models.CharField(max_length=160, default="AR Solutions")
    tagline = models.CharField(
        max_length=240,
        default="Smart Solutions. Stronger Businesses.",
        blank=True,
    )
    email = models.EmailField(default="sales@arsolutions.com", blank=True)
    phone = models.CharField(max_length=40, blank=True)
    whatsapp = models.CharField(
        max_length=40,
        blank=True,
        help_text="Enter country code and number only, for example 971500000000.",
    )
    website = models.URLField(blank=True)
    address = models.TextField(blank=True)
    google_maps_url = models.URLField(blank=True)
    working_hours = models.CharField(
        max_length=180,
        default="Monday–Saturday, 9:00 AM–6:00 PM",
        blank=True,
    )
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    copyright_text = models.CharField(
        max_length=240,
        default="AR Solutions. All rights reserved.",
        blank=True,
    )

    class Meta:
        verbose_name = "Company Settings"
        verbose_name_plural = "Company Settings"

    def __str__(self):
        return self.company_name

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return None

    @property
    def whatsapp_url(self):
        number = "".join(ch for ch in (self.whatsapp or "") if ch.isdigit())
        return f"https://wa.me/{number}" if number else ""
class ProjectShowcase(models.Model):
    CATEGORY_CHOICES = [
        ("software", "Software Product"),
        ("website", "Website Development"),
        ("portfolio", "Portfolio Website"),
        ("career", "Career Service"),
        ("it", "IT Solution"),
    ]

    STATUS_CHOICES = [
        ("completed", "Completed"),
        ("in_progress", "In Progress"),
        ("coming_soon", "Coming Soon"),
    ]

    title = models.CharField(max_length=160)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
    )

    short_description = models.CharField(
        max_length=300,
    )

    full_description = models.TextField(
        blank=True,
        help_text="Optional detailed project description.",
    )

    client_name = models.CharField(
        max_length=160,
        blank=True,
        help_text="Leave blank when the client name should remain private.",
    )

    image_url = models.URLField(
        blank=True,
        help_text="Old external image URL. Optional.",
    )

    project_url = models.URLField(
        blank=True,
        help_text="Optional live project URL.",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="completed",
    )

    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    completed_date = models.DateField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["sort_order", "-created_at"]
        verbose_name = "Project Showcase"
        verbose_name_plural = "Project Showcase"

    def __str__(self):
        return self.title

    @property
    def cover_media(self):
        cover = self.media_items.filter(
            is_active=True,
            is_cover=True,
            media_type="image",
        ).first()

        if cover:
            return cover

        return self.media_items.filter(
            is_active=True,
            media_type="image",
        ).first()


class ProjectMedia(models.Model):
    MEDIA_TYPE_CHOICES = [
        ("image", "Screenshot / Image"),
        ("video", "Screen Recording / Video"),
    ]

    project = models.ForeignKey(
        ProjectShowcase,
        on_delete=models.CASCADE,
        related_name="media_items",
    )

    title = models.CharField(
        max_length=160,
        blank=True,
        help_text="Example: Dashboard, Accounting, Mobile View.",
    )

    media_type = models.CharField(
        max_length=10,
        choices=MEDIA_TYPE_CHOICES,
        default="image",
    )

    image = CloudinaryField(
        "screenshot",
        resource_type="image",
        folder="ar_solutions/projects/screenshots",
        blank=True,
        null=True,
    )

    video = CloudinaryField(
        "screen recording",
        resource_type="video",
        folder="ar_solutions/projects/videos",
        blank=True,
        null=True,
    )

    is_cover = models.BooleanField(
        default=False,
        help_text="Select one screenshot as the project cover.",
    )

    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "Project Media"
        verbose_name_plural = "Project Media"

    def __str__(self):
        return self.title or f"{self.project.title} media"

    def clean(self):
        super().clean()

        if self.media_type == "image" and not self.image:
            raise ValidationError(
                {"image": "Upload an image for Screenshot / Image."}
            )

        if self.media_type == "video" and not self.video:
            raise ValidationError(
                {"video": "Upload a video for Screen Recording / Video."}
            )

        if self.is_cover and self.media_type != "image":
            raise ValidationError(
                {"is_cover": "Only an image can be used as the cover."}
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

        if self.is_cover:
            ProjectMedia.objects.filter(
                project=self.project,
                is_cover=True,
            ).exclude(pk=self.pk).update(is_cover=False)

    @property
    def media_url(self):
        if self.media_type == "video" and self.video:
            return self.video.url

        if self.image:
            return self.image.url

        return ""