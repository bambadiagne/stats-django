from django import forms

class UploadFileForm(forms.Form):
    articles = forms.FileField()