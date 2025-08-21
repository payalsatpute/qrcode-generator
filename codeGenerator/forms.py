from django import forms


class qrcodeform(forms.Form):
    restaurant_name = forms.CharField(
        max_length=30, 
        label='Restaurant name',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter your Restaurant Name',
        })
        )

    
    restaurant_url = forms.URLField(
        max_length=200,
        label='menu url',
        widget=forms.URLInput(attrs={
            'class':'form-control',
            'placrholder':'Enter Your URL'

        })
        )