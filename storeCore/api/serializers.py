from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.serializers import ModelSerializer

from storeCore.models import Pet


class PetSerializer(ModelSerializer):
    """
    ['id', 'owner', 'name', 'chip_number', 'animal_type', 'animal_brand']
    """

    owner = HyperlinkedRelatedField(
        view_name='pet_detail',  # This can be changed to the movies_detail_pk to show the pk link
        read_only=True,
        lookup_field='pk'  # This needs to also be changed for the pk link
    )

    class Meta:
        model = Pet
        fields = ('owner', 'name', 'chip_number', 'animal_type', 'animal_brand')


class OwnerSerializer(ModelSerializer):
    """
    ['id', 'password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined', 'avatar', 'email', 'phone_number', 'user_ptr']
    """
