from rest_framework import viewsets, permissions
from .models import StatusLog
from .serializers import StatusLogSerializer

class StatusLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StatusLog.objects.all()
    serializer_class = StatusLogSerializer
    permission_classes = [permissions.IsAuthenticated]
