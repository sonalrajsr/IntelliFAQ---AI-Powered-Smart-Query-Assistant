from django.db import models
from datetime import datetime

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    embedding = models.JSONField(null=True, blank=True)
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.question

class InteractionLog(models.Model):
    user_query = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"Query: {self.user_query[:50]}... | Response: {self.response[:50]}...| Date: {self.timestamp}"
