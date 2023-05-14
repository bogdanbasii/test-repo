from django.db import models
from django.contrib.auth import get_user_model
from book.models import Book


# Create your models here.

class Purchase(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='purchases', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='purchases', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'purchase'

    def __str__(self):
        return f"{self.user}: {self.book} {self.date}"
