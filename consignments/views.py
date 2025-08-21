from rest_framework import viewsets, permissions
from .models import Consignment
from .serializers import ConsignmentSerializer
from status_logs.models import StatusLog

class ConsignmentViewSet(viewsets.ModelViewSet):
    queryset = Consignment.objects.all()
    serializer_class = ConsignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Consignment.objects.all()
        return Consignment.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def perform_update(self, serializer):
        old_status = serializer.instance.status
        updated_instance = serializer.save()
        new_status = updated_instance.status

        if old_status != new_status:
            StatusLog.objects.create(
                consignment=updated_instance,
                status=new_status,
                changed_by=self.request.user
            )

        
# get_queryset() filters based on role:
# Admins see everything
# Agents/Clients see only their own
# perform_create() auto-assigns the logged-in user as owner
