# file_upload/models.py

from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    text = models.TextField(blank=True)
    expiration_time = models.DateTimeField()
    