from django import forms
from .models import Yorum

class YorumForm(forms.ModelForm):
    class Meta:
        model = Yorum
        fields = ['icerik']