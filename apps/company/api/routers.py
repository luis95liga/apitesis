from django.urls import URLPattern
from django.urls import path,include,re_path
from rest_framework.routers import DefaultRouter
from apps.company.api.views.general_view import (
    CountryViewSet,
    DocumentsCompany,
    ProvinceViewSet,
    LocalityViewSet,
    DocumentTypeViewSet,
    DocumentsViewSet
)
from apps.company.api.views.company_view import (
    CompanyViewSet,
    BankAccountsViewSet,
    TypeCompanyViewSet,
    BankAccountCompany,
    CompanyName
)

router = DefaultRouter()

router.register(r'country',CountryViewSet, basename= 'country')
router.register(r'province',ProvinceViewSet,basename='province')
router.register(r'locality',LocalityViewSet,basename='locality')
router.register(r'documenttypeCompany',DocumentTypeViewSet,basename='documenttype')
router.register(r'documentscompany',DocumentsViewSet,basename='documentscomany')
router.register(r'company',CompanyViewSet,basename='company')
router.register(r'bankaccounts',BankAccountsViewSet,basename='bankaccounts')
router.register(r'typecompany',TypeCompanyViewSet,basename='typecompany')

urlpatterns = [
    path('bankaccountscompany/<int:pk>/', BankAccountCompany.as_view(), name='bankaccountscompany'),
    path('companydocumet/<int:pk>/', DocumentsCompany.as_view(), name='companydocumet'),
    path('companyname/<int:pk>/', CompanyName.as_view(), name='companyname'),
]
urlpatterns += router.urls