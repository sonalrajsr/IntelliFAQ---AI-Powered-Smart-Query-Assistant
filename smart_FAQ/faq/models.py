from django.db import models

class FAQ(models.Model):
    question = models.TextField(unique=True)
    answer = models.TextField()

    def __str__(self):
        return self.question

class InteractionLog(models.Model):
    user_query = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query: {self.user_query[:50]}... | Response: {self.response[:50]}...| Date: {self.timestamp}"
