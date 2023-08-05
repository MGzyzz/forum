from django import forms
from forum.models import Theme, Comment


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        required=False,
        label='Найти',
        widget=forms.TextInput(attrs={
            'class': 'form-control my-3',
            'placeholder': 'enter search value'
        })
    )



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'themes', 'text']

class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields  = ['user', 'title', 'description']
        widgets = {
            'user': forms.HiddenInput(attrs={'class': 'form-control mb-3'}),
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.TextInput(attrs={'class': 'form-control mb-3'})
        }
