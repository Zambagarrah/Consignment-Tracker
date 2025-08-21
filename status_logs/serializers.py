from rest_framework import serializers
from .models import StatusLog

class StatusLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusLog
        fields = '__all__'
