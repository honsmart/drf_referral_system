from django.shortcuts import render
from .serializers import UserSerializers
from .models import Users
from rest_framework import viewsets
# Create your views here.

# Creates/edits the UserProfile database model
class UserViewSet(viewsets.ModelViewSet):
    # Database model
    queryset = Users.objects.all()
    # Serializer - this performs the actions on the queried database entry
    serializer_class = UserSerializers
    # What field in database model will be used to search
    lookup_field = 'user_name'