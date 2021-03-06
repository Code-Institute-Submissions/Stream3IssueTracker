from django import forms
from .models import UaBug, BugPost


class UaBugForm(forms.ModelForm):
    name = forms.CharField(label="Bug name")
    is_a_poll = forms.BooleanField(label=('Include a poll?'),
                                   widget=forms.HiddenInput(), required=False, initial=True)

    class Meta:
        model = UaBug
        fields = ['name']


class PostForm(forms.ModelForm):
    class Meta:
        model = BugPost
        fields = ['comment']
