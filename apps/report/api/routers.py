from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.report.api.view.report_view import ReportPdf,ReportReceptionPdf

router = DefaultRouter()

urlpatterns = [
    path('travelpdf/<int:pk>/<int:idcompany>/', ReportPdf.as_view(), name='travelpdf'),
    path('receptiompdf/<int:pk>/<int:idcompany>/', ReportReceptionPdf.as_view(), name='receptiompdf'),
]

urlpatterns += router.urls