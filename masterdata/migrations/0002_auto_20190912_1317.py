# Generated by Django 2.0.2 on 2019-09-12 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='subdistrict',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]