# Generated by Django 3.0.7 on 2020-06-15 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200614_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='subjects',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
