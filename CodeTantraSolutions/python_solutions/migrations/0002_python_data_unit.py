# Generated by Django 5.0.1 on 2024-01-22 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_solutions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='python_data',
            name='Unit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]
