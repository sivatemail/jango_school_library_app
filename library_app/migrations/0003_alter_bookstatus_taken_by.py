# Generated by Django 4.1.2 on 2022-12-07 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library_app', '0002_bookstatus_renewal_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstatus',
            name='taken_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]
