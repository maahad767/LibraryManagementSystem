# Generated by Django 3.1.4 on 2021-02-04 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copy',
            name='status',
            field=models.CharField(choices=[('available', 'available'), ('borrowed', 'borrowed')], max_length=50),
        ),
    ]
