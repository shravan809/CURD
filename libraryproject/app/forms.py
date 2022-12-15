from django import forms
from .models import Students,issue_book
from django.forms.widgets import NumberInput


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'



class Issue_book(forms.ModelForm):
    class Meta:
        model = issue_book
        fields = ['student','book_title','book_author','issue_date']
        widgets = {
            'student': forms.Select(attrs={'class':'form-group'}),
            'book_title': forms.TextInput(attrs={'class': 'form-group'}),
            'book_author': forms.TextInput( attrs={'class': 'form-group'}),
            'issue_date':forms.NumberInput(attrs={'class':'form-group','type':'date'})
        }
