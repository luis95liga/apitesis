from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.employees.api.views.general_views import DocumentTypeViewSet, PeriodPaymentViewSet, PositionViewSet, PositionTypeViewSet, LaborPaymentsViewSet
from apps.employees.api.views.employee_views import DocumentsEmployee, EmployeePosition, EmployeeViewSet, DocumentEmployeeViewSet,IsLoginViewSet, IsloginEmployee

router = DefaultRouter()
router.register(r'employee',EmployeeViewSet, basename= 'employe')
router.register(r'islogin',IsLoginViewSet, basename= 'islogin')
router.register(r'documenttypee',DocumentTypeViewSet, basename= 'documenttypeee')
router.register(r'documents',DocumentEmployeeViewSet, basename= 'documents')
router.register(r'periodpayment',PeriodPaymentViewSet, basename= 'periodpayment')
router.register(r'positiontype',PositionTypeViewSet, basename= 'positiontype')
router.register(r'position',PositionViewSet, basename= 'position')
router.register(r'laborpayments',LaborPaymentsViewSet, basename= 'laborpayments')
router.register(r'islogin',IsLoginViewSet, basename= 'islogin')

urlpatterns = [
    path('documentemployee/<int:pk>/', DocumentsEmployee.as_view(), name='documentemployee'),
    path('isloginemployee/<int:pk>/', IsloginEmployee.as_view(), name='documentemployee'),
    path('employeeposition/<int:pk>/', EmployeePosition.as_view(), name='employeeposition'),
]
urlpatterns += router.urls

