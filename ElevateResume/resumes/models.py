from django.db import models

class Resume(models.Model):
    content = models.TextField()
    keywords = models.JSONField()

    def __str__(self):
        return self.content[:50]
