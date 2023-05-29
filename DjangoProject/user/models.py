from django.db import models

from purchase.models import Purchase


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(null=False)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name}"

    def get_purchases_count(self):
        return Purchase.objects.filter(id=self.id).count()
