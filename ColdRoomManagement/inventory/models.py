from django.db import models
from django.contrib.auth.models import User

class Material(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    expiry_date = models.DateField()
    received_date = models.DateField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['expiry_date']
