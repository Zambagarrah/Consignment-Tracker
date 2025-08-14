from rest_framework import viewsets, permissions
from .models import Consignment
from .serializers import ConsignmentSerializer

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
        
# get_queryset() filters based on role:
# Admins see everything
# Agents/Clients see only their own
# perform_create() auto-assigns the logged-in user as owner
