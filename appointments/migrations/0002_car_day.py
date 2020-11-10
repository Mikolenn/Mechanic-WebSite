# Generated by Django 3.1.3 on 2020-11-10 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='day',
            field=models.PositiveIntegerField(choices=[(1, 'Lunes'), (2, 'Martes'), (3, 'Miércoles'), (4, 'Jueves'), (5, 'Viernes')], default=0),
            preserve_default=False,
        ),
    ]
