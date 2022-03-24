from django.shortcuts import render
from rest_framework import generics
from .serializers import TodoSerializer # import our serializer
from .models import Todo # import our model

# Create your views here.
# C (add)
# R (view)
class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all().order_by('id') # order the objects that are being retrieved in ascending order by id
    serializer_class = TodoSerializer # which serializer we want to use
# U (update)
# D (delete)
class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    # lines 10-11 === 16-17
    queryset = Todo.objects.all().order_by('id')
    serializer_class = TodoSerializer
