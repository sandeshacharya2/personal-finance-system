from django.db import models
from django.conf import settings

class Bill(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    file = models.FileField(upload_to='bills/')  # File will be saved in MEDIA_ROOT/bills/
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
