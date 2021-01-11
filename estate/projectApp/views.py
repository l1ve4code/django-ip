from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
# Create your views here.

# Rayoni

class RayoniCreateView(generics.CreateAPIView):
  serializer_class = RayoniDetailSerializer

class RayoniListView(generics.ListAPIView):
  serializer_class = RayoniListSerializer
  queryset = Rayoni.objects.all()

class RayoniDetailView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = RayoniDetailSerializer
  queryset = Rayoni.objects.all()

# Gorod

class GorodCreateView(generics.CreateAPIView):
  serializer_class = GorodDetailSerializer

class GorodListView(generics.ListAPIView):
  serializer_class = GorodListSerializer
  queryset = Gorod.objects.all()

class GorodDetailView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = GorodDetailSerializer
  queryset = Gorod.objects.all()

# Operahii

class OperahiiCreateView(generics.CreateAPIView):
  serializer_class = OperahiiDetailSerializer

class OperahiiListView(generics.ListAPIView):
  serializer_class = OperahiiListSerializer
  queryset = Operahii.objects.all()

class OperahiiDetailView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = OperahiiDetailSerializer
  queryset = Operahii.objects.all()

# Role

class RoleCreateView(generics.CreateAPIView):
  serializer_class = RoleDetailSerializer

class RoleListView(generics.ListAPIView):
  serializer_class = RoleListSerializer
  queryset = Role.objects.all()

class RoleDetailView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = RoleDetailSerializer
  queryset = Role.objects.all()

# Polzovateli

class PolzovateliCreateView(generics.CreateAPIView):
  serializer_class = PolzovateliDetailSerializer

class PolzovateliListView(generics.ListAPIView):
  serializer_class = PolzovateliListSerializer
  queryset = Polzovateli.objects.all()

class PolzovateliDetailView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = PolzovateliDetailSerializer
  queryset = Polzovateli.objects.all()

# Predlozheniya

class PredlozheniyaCreateView(generics.CreateAPIView):
  serializer_class = PredlozheniyaDetailSerializer

class PredlozheniyaListView(generics.ListAPIView):
  serializer_class = PredlozheniyaListSerializer
  queryset = Predlozheniya.objects.all()

class PredlozheniyaDetailView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = PredlozheniyaDetailSerializer
  queryset = Predlozheniya.objects.all()

# Tariphy

class TariphyCreateView(generics.CreateAPIView):
  serializer_class = TariphyDetailSerializer

class TariphyListView(generics.ListAPIView):
  serializer_class = TariphyListSerializer
  queryset = Tariphy.objects.all()

class TariphyDetailView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = TariphyDetailSerializer
  queryset = Tariphy.objects.all()

# Spros

class SprosCreateView(generics.CreateAPIView):
  serializer_class = SprosDetailSerializer

class SprosListView(generics.ListAPIView):
  serializer_class = SprosListSerializer
  queryset = Spros.objects.all()

class SprosDetailView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = SprosDetailSerializer
  queryset = Spros.objects.all()

# Straxovoi

class StraxovoiCreateView(generics.CreateAPIView):
  serializer_class = StraxovoiDetailSerializer

class StraxovoiListView(generics.ListAPIView):
  serializer_class = StraxovoiListSerializer
  queryset = Straxovoi.objects.all()

class StraxovoiDetailView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = StraxovoiDetailSerializer
  queryset = Straxovoi.objects.all()

# Sdelki

class SdelkiCreateView(generics.CreateAPIView):
  serializer_class = SdelkiDetailSerializer

class SdelkiListView(generics.ListAPIView):
  serializer_class = SdelkiListSerializer
  queryset = Sdelki.objects.all()

class SdelkiDetailView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = SdelkiDetailSerializer
  queryset = Sdelki.objects.all()