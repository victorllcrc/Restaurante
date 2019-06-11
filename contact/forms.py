from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control'}
    ))
    content = forms.CharField(label="contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control'}
    ))