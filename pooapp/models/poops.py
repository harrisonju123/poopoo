from django.db import models


class Poops(models.Model):
    date = models.DateTimeField()
    user_id =models.CharField(max_length=64)
    difficulty = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.date} - {self.difficulty}"
