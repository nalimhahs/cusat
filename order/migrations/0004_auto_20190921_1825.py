# Generated by Django 2.2.5 on 2019-09-21 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20190921_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='assigned_driver',
            field=models.ForeignKey(blank=True, limit_choices_to={'user_type': 'D'}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Driver', to=settings.AUTH_USER_MODEL),
        ),
    ]
