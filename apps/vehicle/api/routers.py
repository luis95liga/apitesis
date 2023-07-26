from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.vehicle.api.views.vehicle_views import (
    AssignVehicleTrailer,
    CreateTrailer,
    CreateVehicle,
    VehicleViewSet,
    TechnicalDataViewSet,
    VehicleModelViewSet,
    TechnicalDataTrailerViewSet,
    TrailerViewSet,
    DocumentVehicleViewSet,
    DocumentsVehicle,
    AssignTrailerViewSet,
    FixedCostsViewSet,
    FixedCostsVehicle
)
from apps.vehicle.api.views.general_views import (
    GeneralDataVehicle,
    MaintenamceCostsVehicle,
    OwnerViewSet,
    VehicleUseViewSet,
    AxesViewSet,
    ManufacturerViewSet,
    VehicleTypeViewSet,
    FuelViewSet,
    GeneralDataViewSet,
    MaintenamceCostsViewSet,
    DocumentTypeViewSet
    )

router = DefaultRouter()

router.register(r'vehicle',VehicleViewSet, basename= 'vehicle')
router.register(r'technicaldatatraile',TechnicalDataTrailerViewSet,basename='technicaldatatrailer')
router.register(r'trailer',TrailerViewSet, basename= 'trailer')
router.register(r'technicaldata',TechnicalDataViewSet,basename='technicaldata')
router.register(r'vehiclemodel',VehicleModelViewSet,basename='vehiclemodel')
router.register(r'owner',OwnerViewSet,basename='ower')
router.register(r'vehicleuse',VehicleUseViewSet,basename='vehicleuse')
router.register(r'axes',AxesViewSet,basename='axes')
router.register(r'manufacturer',ManufacturerViewSet,basename='manufacturer')
router.register(r'vehicletype',VehicleTypeViewSet,basename='vehicletype')
router.register(r'fuel',FuelViewSet,basename='fuel')
router.register(r'generaldata',GeneralDataViewSet,basename='generaldata')
router.register(r'maintenamcecosts',MaintenamceCostsViewSet,basename='maintenamcecosts')
router.register(r'document',DocumentVehicleViewSet,basename='document')
router.register(r'vehicledocumenttype',DocumentTypeViewSet,basename='vehicledocumenttype')
router.register(r'assigntrailer',AssignTrailerViewSet,basename='assigntrailer')
router.register(r'fixedcosts',FixedCostsViewSet,basename='fixedcosts')

urlpatterns = [
    path('generaldatavehicle/<int:pk>/', GeneralDataVehicle.as_view(), name='generaldatavehicle'),
    path('documentvehicle/<int:pk>/', DocumentsVehicle.as_view(), name='documentvehicle'),
    path('maintenamcecostsvehicle/<int:pk>/', MaintenamceCostsVehicle.as_view(), name='generaldatavehicle'),
    path('vehiclecreate/', CreateVehicle.as_view(), name='vehiclecreate'),
    path('trailercreate/', CreateTrailer.as_view(), name='trailercreate'),
    path('assignaehicletrailer/<int:pk>/', AssignVehicleTrailer.as_view(), name='assignaehicletrailer'),
    path('fixedcostsvehicle/<int:pk>/', FixedCostsVehicle.as_view(), name='fixedcostsvehicle')
]

urlpatterns += router.urls

