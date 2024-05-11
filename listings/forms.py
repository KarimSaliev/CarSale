from django import forms
from listings.models import Car, Category

class CarForm(forms.Form):
    CHOICES = [(category.id, category.name) for category in Category.objects.all()]
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Name of the car',
        'required': True,
    }))
    brand = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Brand of the car',
        'required': True,
    }))

    type = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Type of the car',
            'required': True,
        })
    )
    image1 = forms.FileField(required=True, widget=forms.ClearableFileInput(attrs={
        'class': 'form-control', 'placeholder': 'Insert the car\'s pictures ',
    }))
    image2 = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={
        'class': 'form-control', 'placeholder': 'Insert the car\'s pictures ',
    }))
    image3 = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={
        'class': 'form-control', 'placeholder': 'Insert the car\'s pictures ',
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Provide a description',
    }))
    color = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Color of your car',
    }))
    condition = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Indicate your car\'s condition',

    }))
    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Indicate price',
            'required': True,
        }))
    number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Your phone number'
    }), required=True)

    class Meta:
        model = Car
        fields = ('name','brand','type','image1','image2','image3','description', 'color', 'condition','price', 'number')


class CarSearch(forms.Form):
    price_ranges = ((1000,'Up to 1000'), (5000,'Up to 5000'), (100000,'Up to 100000'),)
    types = [(category.id, category.name) for category in Category.objects.all()]
    brand = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Brand'}), required=True)

    type = forms.ChoiceField(
        choices=types,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Type',

        }), required=False
    )
    price = forms.ChoiceField(
        choices=price_ranges,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Price',

        }), required=False
    )
    color = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Color'
    }), required=False)
    class Meta:
        model = Car
        fields = ('brand', 'price', 'type' 'color')