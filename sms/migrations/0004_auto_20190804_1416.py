# Generated by Django 2.0.2 on 2019-08-04 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthfacility', '0001_initial'),
        ('sms', '0003_caseinformation_is_pregnant'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('message_type', models.CharField(choices=[('inbox', 'Inbox'), ('sentbox', 'Sentbox')], default='inbox', max_length=15)),
                ('case_information', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_information', to='sms.CaseInformation')),
                ('destination_facility', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='destination_facility', to='healthfacility.HealthFacility')),
                ('origin_facility', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='origin_facility', to='healthfacility.HealthFacility')),
            ],
            options={
                'db_table': 'message_information',
            },
        ),
        migrations.AlterUniqueTogether(
            name='messageinformation',
            unique_together={('case_information', 'origin_facility', 'destination_facility', 'message_type')},
        ),
    ]
