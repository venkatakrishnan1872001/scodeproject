

from .views import BlogList,BlogDetailbyID,ScodeServiceList
from django.urls import path


urlpatterns = [
    path('blogList/', BlogList.as_view(),name="blogList"),
    path('blogbyId/', BlogDetailbyID.as_view(),name="BlogDetailbyID"),
    path('ScodeDetail', ScodeServiceList.as_view(), name='ScodeList'),
]