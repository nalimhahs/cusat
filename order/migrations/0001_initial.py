# Generated by Django 2.2.5 on 2019-09-21 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
                ('weight', models.IntegerField()),
                ('date_of_order', models.DateField()),
                ('assigned_driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='driver.Driver')),
            ],
        ),
    ]
