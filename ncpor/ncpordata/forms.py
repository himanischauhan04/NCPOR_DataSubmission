from django import forms
from ncpordata.models import Metadata

class MetadataForm(forms.ModelForm):

    class Meta:
        model = Metadata
        fields = '__all__'
        widgets = {
            'expedition_type': forms.RadioSelect,
            'gps': forms.RadioSelect,
            'abstract': forms.Textarea(attrs={'rows': 3}),
            'purpose': forms.Textarea(attrs={'rows': 3}),
            'institute': forms.Textarea(attrs={'rows': 2}),
            'address': forms.Textarea(attrs={'rows': 2}),
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            # Skip fields like RadioSelect which use a different class
            if isinstance(field.widget, (forms.TextInput, forms.Select, forms.Textarea, forms.DateInput, forms.NumberInput)):
                existing_class = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_class} form-control".strip()
