from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from ..models import Pet
from .serializers import PetSerializer


class PetList(ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetDetailPK(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = Pet.objects.all()
    serializer_class = PetSerializer