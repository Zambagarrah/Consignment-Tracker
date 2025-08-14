from rest_framework import serializers
from .models import Consignment

class ConsignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consignment
        fields = '__all__'
        read_only_fields = ['owner', 'created_at', 'updated_at']

# __all__ includes every field
# owner, created_at, and updated_at are read-only — they’re auto-assigned