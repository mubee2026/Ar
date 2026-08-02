from django import forms
from .models import DemoRequest, ContactEnquiry

class StyledModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-control")


class DemoRequestForm(StyledModelForm):
    class Meta:
        model = DemoRequest
        fields = ["name", "company", "email", "phone", "company_type", "users", "requirements"]
        widgets = {"requirements": forms.Textarea(attrs={"rows": 5})}


class ContactEnquiryForm(StyledModelForm):
    class Meta:
        model = ContactEnquiry
        fields = ["name", "company", "email", "phone", "subject", "message"]
        widgets = {"message": forms.Textarea(attrs={"rows": 5})}
