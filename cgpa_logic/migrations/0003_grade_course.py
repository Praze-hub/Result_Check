# Generated by Django 3.2.21 on 2024-01-05 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cgpa_logic', '0002_auto_20240105_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='cgpa_logic.course'),
        ),
    ]
