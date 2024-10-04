from django.urls import path
from .views import СatListApiView, BreedListApiView, CatFilterApiView, CatRetrieveApiView

urlpatterns = [
    path('', СatListApiView.as_view(), name='list'),
    path('<int:id>/', CatRetrieveApiView.as_view(), name='cat'),
    path('filter/', CatFilterApiView.as_view(), name='filter'),
    path('breeds/', BreedListApiView.as_view(), name='breeds')
]
