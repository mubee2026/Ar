from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.products, name="products"),
    path("products/engicore-erp/", views.engineering_erp, name="engineering_erp"),
    path("pricing/", views.pricing, name="pricing"),
    path("demo/", views.demo, name="demo"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("support/", views.support, name="support"),
    path("privacy/", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
    path("refund/", views.refund, name="refund"),
]
