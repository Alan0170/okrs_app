from django import forms
from .models import Okr


class OkrForm(forms.ModelForm):
    class Meta:
        model = Okr
        fields = "__all__"
