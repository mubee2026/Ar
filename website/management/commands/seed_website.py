from django.core.management.base import BaseCommand
from website.models import Product, PricingPlan

class Command(BaseCommand):
    help = "Create default AR Solutions product and pricing data."

    def handle(self, *args, **options):
        Product.objects.get_or_create(
            slug="engicore-erp",
            defaults={
                "name": "EngiCore ERP",
                "short_description": "Commercial Engineering ERP for projects, accounting, purchase and inventory.",
                "description": "Professional ERP for engineering and project-based companies.",
                "is_featured": True,
                "sort_order": 1,
            },
        )
        plans = [
            ("Starter", "For small teams beginning digital operations.", "Contact", "Core ERP modules\nSingle company\nBasic setup\nStandard support", False, 1),
            ("Professional", "For established engineering businesses.", "Custom", "All core modules\nUser roles and audit\nPDF and Excel reports\nImplementation and training", True, 2),
            ("Enterprise", "For larger teams and advanced workflows.", "Tailored", "Custom workflow development\nData migration\nPriority support\nAdvanced deployment", False, 3),
        ]
        for name, subtitle, price, features, featured, order in plans:
            PricingPlan.objects.get_or_create(
                name=name,
                defaults={
                    "subtitle": subtitle,
                    "price_label": price,
                    "features": features,
                    "is_featured": featured,
                    "sort_order": order,
                },
            )
        self.stdout.write(self.style.SUCCESS("Default website data created."))
