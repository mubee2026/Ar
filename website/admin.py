from django.contrib import admin
from .models import Product, PricingPlan, DemoRequest, ContactEnquiry, CompanySettings

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "is_featured", "is_active", "sort_order")
    list_editable = ("is_featured", "is_active", "sort_order")
    search_fields = ("name", "short_description")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ("name", "price_label", "is_featured", "is_active", "sort_order")
    list_editable = ("price_label", "is_featured", "is_active", "sort_order")

@admin.register(DemoRequest)
class DemoRequestAdmin(admin.ModelAdmin):
    list_display = ("company", "name", "phone", "company_type", "users", "status", "created_at")
    list_filter = ("status", "company_type", "users", "created_at")
    search_fields = ("company", "name", "email", "phone")
    list_editable = ("status",)
    readonly_fields = ("created_at",)

@admin.register(ContactEnquiry)
class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display = ("subject", "name", "company", "email", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("subject", "name", "company", "email", "phone")
    list_editable = ("status",)
    readonly_fields = ("created_at",)

admin.site.site_header = "AR Solutions Website Administration"
admin.site.site_title = "AR Solutions Admin"
admin.site.index_title = "Website Management"


@admin.register(CompanySettings)
class CompanySettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Brand", {
            "fields": ("company_name", "tagline", "website"),
        }),
        ("Contact", {
            "fields": ("email", "phone", "whatsapp", "address", "google_maps_url", "working_hours"),
        }),
        ("Social Media", {
            "fields": ("facebook_url", "instagram_url", "linkedin_url", "youtube_url"),
        }),
        ("Footer", {
            "fields": ("copyright_text",),
        }),
    )

    def has_add_permission(self, request):
        return not CompanySettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
