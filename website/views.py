from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import ContactEnquiryForm, DemoRequestForm
from .models import PricingPlan, Product,ProjectShowcase


def home(request):
    return render(request, "website/home.html")


def products(request):
    items = Product.objects.filter(is_active=True)

    showcases = ProjectShowcase.objects.filter(
        is_active=True,
    )

    context = {
        "products": items,
        "software_projects": showcases.filter(
            category="software",
        ),
        "website_projects": showcases.filter(
            category="website",
        ),
        "portfolio_projects": showcases.filter(
            category="portfolio",
        ),
        "career_projects": showcases.filter(
            category="career",
        ),
        "it_projects": showcases.filter(
            category="it",
        ),
    }

    return render(
        request,
        "website/products.html",
        context,
    )


def engineering_erp(request):
    return render(request, "website/engineering_erp.html")


def pricing(request):
    plans = PricingPlan.objects.filter(is_active=True)
    return render(request, "website/pricing.html", {"plans": plans})


def demo(request):
    form = DemoRequestForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        enquiry = form.save()

        try:
            send_mail(
                subject=f"New Demo Request - {enquiry.company}",
                message=(
                    f"Name: {enquiry.name}\n"
                    f"Company: {enquiry.company}\n"
                    f"Email: {enquiry.email}\n"
                    f"Phone: {enquiry.phone}\n"
                    f"Company Type: "
                    f"{enquiry.get_company_type_display()}\n"
                    f"Users: {enquiry.get_users_display()}\n\n"
                    f"Requirements:\n{enquiry.requirements}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.SALES_NOTIFICATION_EMAIL],
                fail_silently=True,
            )
        except Exception:
            pass

        return redirect("thank_you", submission_type="demo")

    return render(request, "website/demo.html", {"form": form})


def contact(request):
    form = ContactEnquiryForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        enquiry = form.save()

        try:
            send_mail(
                subject=f"Website Enquiry - {enquiry.subject}",
                message=(
                    f"Name: {enquiry.name}\n"
                    f"Company: {enquiry.company}\n"
                    f"Email: {enquiry.email}\n"
                    f"Phone: {enquiry.phone}\n\n"
                    f"Message:\n{enquiry.message}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.SALES_NOTIFICATION_EMAIL],
                fail_silently=True,
            )
        except Exception:
            pass

        return redirect("thank_you", submission_type="enquiry")

    return render(request, "website/contact.html", {"form": form})


def thank_you(request, submission_type):
    allowed_types = {
        "enquiry": {
            "title": "Enquiry Submitted",
            "message": (
                "Thank you for contacting AR Solutions. "
                "Your enquiry has been received successfully."
            ),
        },
        "demo": {
            "title": "Demo Request Submitted",
            "message": (
                "Thank you for requesting a software demo. "
                "Your request has been received successfully."
            ),
        },
    }

    submission = allowed_types.get(
        submission_type,
        allowed_types["enquiry"],
    )

    return render(
        request,
        "website/thank_you.html",
        {"submission": submission},
    )


def about(request):
    return render(request, "website/about.html")


def support(request):
    return render(request, "website/support.html")


def privacy(request):
    return render(request, "website/privacy.html")


def terms(request):
    return render(request, "website/terms.html")


def refund(request):
    return render(request, "website/refund.html")


def custom_404(request, exception):
    return render(
        request,
        "website/404.html",
        status=404,
    )