from django.urls import URLPattern
from django.urls import path,include,re_path
from rest_framework.routers import DefaultRouter
from apps.routes.api.views.routers_view import (
    CellarsViewSet,
    DestinationViewSet,
    TabulationViewSet,
    TabulationCompany,
    BillViewSet,
    ConceptsViewSet,
    BillCompany,
    TabulationOriginDestination,
    BillTabulation
)

router = DefaultRouter()

router.register(r'cellars',CellarsViewSet, basename= 'cellar')
router.register(r'destination',DestinationViewSet,basename='destination')
router.register(r'tabulation',TabulationViewSet,basename='tabulation')
router.register(r'bill',BillViewSet,basename='bill')
router.register(r'concepts',ConceptsViewSet,basename='concepts')

urlpatterns = [
    path('tabulationcompany/<int:pk>/', TabulationCompany.as_view(), name='tabulationcompany'),
    path('tabulationorigindestination/<int:pk>/<int:pk1>/<int:pk2>/', TabulationOriginDestination.as_view(), name='tabulationorigindestination'),
    path('billcompany/<int:pk>/<int:pk1>/', BillCompany.as_view(), name='billcompany'),
    path('billtabulation/', BillTabulation.as_view(), name='billtabulation')
]

urlpatterns += router.urls