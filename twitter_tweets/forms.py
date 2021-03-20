from django import forms


class TweetForm(forms.Form):
    content = forms.CharField(max_length=140)
