# Generated by Django 5.1.1 on 2024-10-04 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='comment',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]
