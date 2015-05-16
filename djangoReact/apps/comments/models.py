from django.db import models


class Comment(models.Model):
    author = models.CharField(max_length=40)
    text = models.TextField(max_length=140)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.text
