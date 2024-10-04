from django.urls import path
from .views import СatListApiView, BreedListApiView

urlpatterns = [
    path('', СatListApiView.as_view(), name='list'),
    path('breeds/', BreedListApiView.as_view(), name='breeds')
]
