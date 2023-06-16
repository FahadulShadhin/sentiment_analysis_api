import uuid
from django.db import models


class SentimentModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField(max_length=255)
    sentiment = models.CharField(max_length=128, default="")
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "sentiments"
        ordering = ['-createdAt']

    def __str__(self) -> str:
        return str(self.id)
