from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.guide.api.view.guide_view import *

router = DefaultRouter()

router.register(r'guide', GuideViewSet, basename= 'guide')
router.register(r'travel', TravelViewSet, basename= 'travel')
router.register(r'guidecontent', GuideContentViewSet, basename= 'guidecontent')
router.register(r'guidecontentdetail', GuideContentDetailViewSet, basename= 'guidecontentdetail')
router.register(r'guidecontentdetailtmp', GuideContentDetailTmpViewSet, basename= 'guidecontentdetailtmp')
router.register(r'unit', UnitViewSet, basename= 'unit')
router.register(r'invoicetype', InvoiceTypeViewSet, basename= 'invoicetype')

urlpatterns = [
    path('guidedeactivate/<int:idcompany>/<int:iduser>/<int:idvehicle>/', GuideListFalseView.as_view(), name='gride'),
    path('guideactivate/<int:pk>/', GuideListTrueView.as_view(), name='gride'),
    path('guidelocationlatitude/<int:pk>/', GuideLocationLatitudeView.as_view(), name='guidelocationlatitude'),
    path('guidedetailsview/<int:pk>/', GuideDeailView.as_view(), name='guidedetailview'),
]

urlpatterns += router.urls