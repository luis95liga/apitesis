from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path,include,re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from apps.users.views import Login,Logout, PasswordResetView, ResetPasswordAPIView
from drf_yasg import openapi

from django.conf import settings

schema_view = get_schema_view(
   openapi.Info(
      title="Documetacion API",
      default_version='v0.1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="luis95liga@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('login/',Login.as_view(),name= 'login'),
    path('logout/',Logout.as_view(),name= 'logout'),
    path('reset-password/', PasswordResetView.as_view(),name= 'reset-password'),
    path('reset-password/<str:encoded_pk>/<str:token>/', ResetPasswordAPIView.as_view(),name= 'reset-password'),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include("apps.index.urls")),
    path('admin/', admin.site.urls),
    path('user/',include('apps.users.api.routers'),name='user'),
    path('vehicle/',include('apps.vehicle.api.routers'),name='vehicle'),
    path('company/',include('apps.company.api.routers'),name='company'),
    path('employee/',include('apps.employees.api.routers'), name='employee'),
    path('route/',include('apps.routes.api.routers'), name='employee'),
    path('clients/',include('apps.client.api.routers'), name='client'),
    path('guide/',include('apps.guide.api.routers'), name='guide'),
    path('report/',include('apps.report.api.routers'), name='report'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

