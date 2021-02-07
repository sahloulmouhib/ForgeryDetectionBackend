from django import forms
from django.db import models
#from task2.tasks import send_review_email_task



class ReviewForm(forms.Form):
    firstName = forms.CharField(
        label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-firstname'}))
    email = forms.EmailField(
        max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'E-mail', 'id': 'form-email'}))
    review = forms.CharField(
        label="Description", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))
    image=forms.ImageField()

    
    def send_email(self):
                             
        send_review_email_task.delay(
            self.cleaned_data['firstName'], self.cleaned_data['email'], self.cleaned_data['review'])
