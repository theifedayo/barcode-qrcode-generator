from django import forms



class ContentForm(forms.Form):
    content = forms.CharField(max_length=254, help_text='Required. Enter your content')

