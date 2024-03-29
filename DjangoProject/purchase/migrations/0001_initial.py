# Generated by Django 4.2 on 2023-04-13 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='book.book')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='user.user')),
            ],
            options={
                'db_table': 'purchase',
            },
        ),
    ]
