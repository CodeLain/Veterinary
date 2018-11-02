from django.urls import path

from .api_views import PetList, PetDetailPK

urlpatterns = [
    path('my_pets/', PetList.as_view(), name="pet_list"),
    path('my_pets/<int:pk>', PetDetailPK.as_view(), name="pet_detail"),
]