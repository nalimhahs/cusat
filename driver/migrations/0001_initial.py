# Generated by Django 2.2.5 on 2019-09-21 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(blank=True, max_length=20)),
                ('phoneno', models.IntegerField()),
                ('age', models.IntegerField()),
                ('vehiclecarrysize', models.IntegerField()),
                ('licenseno', models.IntegerField()),
                ('vehicleregno', models.IntegerField()),
                ('region', models.CharField(max_length=80)),
            ],
        ),
    ]
