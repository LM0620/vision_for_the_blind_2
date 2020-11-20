# Li Ma: 100%
from django.db import models


class File(models.Model):
    file = models.FileField(blank=False, null=False)
    option = models.CharField(max_length=20, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)