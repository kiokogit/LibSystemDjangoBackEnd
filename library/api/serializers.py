#classes that take a model and turn it into a json object

from rest_framework.serializers import ModelSerializer;
from ..models import Books;

class BookSerializer(ModelSerializer):
    class Meta:
        model=Books;
        fields='__all__';