from django import forms
from .models import Movie


#movie form for creating and updating movie instances

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'release_date', 'genre', 'price', 'director', 'description', 'rating','poster']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'release_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '5'}),
            'poster': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


# Validation for the form fields

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if not name:
            raise forms.ValidationError("Movie name cannot be empty.")
        return name

    def clean_rating(self):
        rating = round(self.cleaned_data['rating'], 1)
        if not 0.0 <= rating <= 5.0:
            raise forms.ValidationError("Rating must be between 0.0 and 5.0.")
        return rating