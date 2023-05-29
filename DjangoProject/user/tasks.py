from celery import shared_task
from django.utils import timezone
from user.models import User


@shared_task
def my_task():
    print('This is my task')

@shared_task
def print_purchases_count(id):
    user = User.objects.get(id=id)
    count = user.get_purchases_count()
    print(f"User {id} has {count} purchases.")

@shared_task
def print_users_count():
    users_count = User.objects.all().count()
    print(f"{timezone.now()}: There are {users_count} users in the database.")