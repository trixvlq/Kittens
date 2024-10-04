from django.urls import path
from .views import СatListApiView, BreedListApiView, CatFilterApiView, CatRetrieveApiView, CatRateApiView, \
    CatCreateApiView

urlpatterns = [
    path('', СatListApiView.as_view(), name='list'),
    path('<int:id>/', CatRetrieveApiView.as_view(), name='cat'),
    path('create/', CatCreateApiView.as_view(), name='create'),
    path('rate/<int:id>/', CatRateApiView.as_view(), name='rate'),
    path('filter/', CatFilterApiView.as_view(), name='filter'),
    path('breeds/', BreedListApiView.as_view(), name='breeds')
]
