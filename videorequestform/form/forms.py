from django import forms


class Vform(forms.Form):
    Name=forms.CharField(max_length=20,widget=forms.TextInput(
        attrs={
            'placeholder':'Video Title',
            'class':"form-control"
        }
    ))
    Description=forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder':'Video Description',
            'class':"form-control",
            'placeholder':"Enter the text",
            'cols':"30",
            'rows':"10" 
        }
    ))