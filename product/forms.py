from django import forms

from .models import Products

class ProductForm(forms.ModelForm):
    title       = forms.CharField(widget = forms.TextInput(attrs = {'placeholder':'please enter your title here'}))
    description = forms.CharField(widget = forms.Textarea(attrs={'class':'new-class',"rows":15,'cols':25}))
    price       =  forms.DecimalField(initial = 0.00)


    class Meta():

        model = Products
        fields = [
            'title',
            'type',
            'description',
            'price',
        ]

    '''def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "damu" not in title:
            raise forms.ValidationError(" Your title should contain damu ")'''

class RawProductForm(forms.Form):

    initial1 = 'This is my phone'

    title       = forms.CharField(widget = forms.TextInput(attrs = {'placeholder':'please enter your title here'}))
    description = forms.CharField(widget = forms.Textarea(attrs={'class':'new-class',"rows":15,'cols':25}))
    price       =  forms.DecimalField(initial = 00)