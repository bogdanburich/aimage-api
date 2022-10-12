from django.core.validators import MinValueValidator
from django.forms import IntegerField, ModelForm


class ImageAdminForm(ModelForm):
    count = IntegerField(required=True, validators=[MinValueValidator(1)])
