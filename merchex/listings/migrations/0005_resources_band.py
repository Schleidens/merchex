# Generated by Django 3.2.16 on 2023-02-17 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_resources_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='band',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.band'),
        ),
    ]
