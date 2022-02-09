from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('locations/', views.LocationList.as_view(), name='location_list'),
    path('locations/<int:pk>', views.LocationDetail.as_view(),
         name='location_detail'),
    path('exhibitions/', views.ExhibitionList.as_view(), name='exhibition_list'),
    path('exhibitions/<int:pk>', views.ExhibitionDetail.as_view(),
         name='exhibition_detail')
]
