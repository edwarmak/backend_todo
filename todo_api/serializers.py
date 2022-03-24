from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer): # convert sql to JSON
    class Meta:
        model = Todo # we are using our Todo model
        fields = ('id', 'title', 'description',) # which fields of our model to include
