# Generated by Django 3.2.16 on 2023-02-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20230216_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
