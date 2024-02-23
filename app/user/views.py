from rest_framework import generics
from user.serializers import userSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = userSerializer
