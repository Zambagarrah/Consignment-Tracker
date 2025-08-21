from django.db import models
from consignments.models import Consignment
from users.models import User

class StatusLog(models.Model):
    consignment = models.ForeignKey(Consignment, on_delete=models.CASCADE, related_name='logs')
    status = models.CharField(max_length=20)
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.consignment.item_name} → {self.status} by {self.changed_by}"
