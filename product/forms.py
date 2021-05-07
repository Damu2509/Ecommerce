from django import forms

class CreateNewList(forms.Form):

    name = forms.CharField( max_length  = 100 )
    check = forms.BooleanField( default =  False ) 


