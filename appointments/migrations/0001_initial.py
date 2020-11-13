# Generated by Django 3.1.3 on 2020-11-13 04:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=20)),
                ('transmission', models.CharField(choices=[('A', 'Automatico'), ('M', 'Manual')], max_length=1)),
                ('year', models.PositiveIntegerField(blank=True)),
                ('brand', models.CharField(max_length=20)),
                ('day', models.CharField(choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miércoles', 'Miércoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes')], max_length=10)),
                ('schedule', models.CharField(choices=[('8:00 am', '8:00 am'), ('9:00 am', '9:00 am'), ('10:00 am', '10:00 am'), ('11:00 am', '11:00 am'), ('1:00 pm', '1:00 pm'), ('2:00 pm', '2:00 pm'), ('3:00 pm', '3:00 pm'), ('4:00 pm', '4:00 pm')], max_length=10)),
                ('date', models.DateField(blank=True)),
                ('provider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provider', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
