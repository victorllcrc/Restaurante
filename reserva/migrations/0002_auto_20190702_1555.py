# Generated by Django 2.1.8 on 2019-07-02 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='fecha',
            field=models.CharField(max_length=255, verbose_name='fecha de reserva'),
        ),
    ]
