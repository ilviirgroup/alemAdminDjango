# Generated by Django 3.0.2 on 2021-01-21 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alemsite', '0010_auto_20210121_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userr', to=settings.AUTH_USER_MODEL),
        ),
    ]
