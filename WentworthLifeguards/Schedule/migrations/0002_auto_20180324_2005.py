# Generated by Django 2.0.3 on 2018-03-24 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shifts',
            name='Employees',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='Schedule.Employees'),
        ),
    ]