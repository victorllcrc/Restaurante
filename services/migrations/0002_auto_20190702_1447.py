# Generated by Django 2.1.8 on 2019-07-02 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='precio',
            field=models.FloatField(verbose_name='Precio'),
        ),
    ]
