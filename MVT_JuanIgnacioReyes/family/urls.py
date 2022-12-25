from django.urls import path
from family.views import create_family_member, list_family_members


urlpatterns = [
    path("create-member/", create_family_member),
    path("list-family/", list_family_members),
]
