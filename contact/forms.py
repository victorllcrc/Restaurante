from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu msnsaje'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu msnsaje'}
    ), min_length=3, max_length=100)
    content = forms.CharField(label="contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'row': 3, 'placeholder':'Escribe tu msnsaje'}
    ), min_length=10, max_length=1000)

    fecha = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }))


