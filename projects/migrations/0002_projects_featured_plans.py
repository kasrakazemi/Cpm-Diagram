# Generated by Django 4.1.5 on 2024-01-21 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='featured_plans',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plan_set', to='projects.plans'),
        ),
    ]
