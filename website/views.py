from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from .forms import DemoRequestForm, ContactEnquiryForm
from .models import Product, PricingPlan

def home(request):
    return render(request, "website/home.html")

def products(request):
    items = Product.objects.filter(is_active=True)
    return render(request, "website/products.html", {"products": items})

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
                    f"Name: {enquiry.name}\nCompany: {enquiry.company}\n"
                    f"Email: {enquiry.email}\nPhone: {enquiry.phone}\n"
                    f"Company Type: {enquiry.get_company_type_display()}\n"
                    f"Users: {enquiry.get_users_display()}\n\n"
                    f"Requirements:\n{enquiry.requirements}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.SALES_NOTIFICATION_EMAIL],
                fail_silently=True,
            )
        except Exception:
            pass
        messages.success(request, "Thank you. Your demo request has been submitted.")
        return redirect("demo")
    return render(request, "website/demo.html", {"form": form})

def contact(request):
    form = ContactEnquiryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        enquiry = form.save()
        try:
            send_mail(
                subject=f"Website Enquiry - {enquiry.subject}",
                message=(
                    f"Name: {enquiry.name}\nCompany: {enquiry.company}\n"
                    f"Email: {enquiry.email}\nPhone: {enquiry.phone}\n\n"
                    f"Message:\n{enquiry.message}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.SALES_NOTIFICATION_EMAIL],
                fail_silently=True,
            )
        except Exception:
            pass
        messages.success(request, "Thank you. Your enquiry has been submitted.")
        return redirect("contact")
    return render(request, "website/contact.html", {"form": form})

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
