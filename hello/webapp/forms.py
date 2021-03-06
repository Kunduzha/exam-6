from django import forms
from webapp.models import Comments

class Commentform(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'email', 'comment', 'status')