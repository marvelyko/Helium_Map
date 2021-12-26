from django.db.models import fields
from django.forms import ModelForm
from .models import Point

class PointForm(ModelForm):
    class Meta:
        model = Point
        fields = "__all__"
        exclude = ["user"]