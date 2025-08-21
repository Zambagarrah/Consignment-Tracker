from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from consignments.views import ConsignmentViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from status_logs.views import StatusLogViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = DefaultRouter()
router.register(r'consignments', ConsignmentViewSet)

urlpatterns += [
    path('api/', include(router.urls)),
]

router.register(r'status-logs', StatusLogViewSet)
