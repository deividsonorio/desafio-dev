from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
import os


class UploadFileForm(forms.Form):
    ALLOWED_TYPES = ['txt']

    file = forms.FileField(
        validators=[
            FileExtensionValidator(allowed_extensions=ALLOWED_TYPES),
        ]
    )

    def clean_file(self):
        file = self.cleaned_data.get('file', None)
        if not file:
            self.add_error('file', 'Arquivo não encontrado')
        try:
            extension = os.path.splitext(file.name)[1][1:].lower()
            if extension in self.ALLOWED_TYPES:
                return file
            else:
                self.add_error('file', 'Arquivo com extensão inválida')
        except Exception as e:
            self.add_error('file', 'Não foi possível identicar o tipo de arquivo: {}'.format(e))


class GenerateRandomUserForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(2),
            MaxValueValidator(500)
        ]
    )
