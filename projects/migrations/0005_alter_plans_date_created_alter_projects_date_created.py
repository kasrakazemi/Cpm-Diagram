# Generated by Django 4.1.5 on 2024-01-25 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_plans_owner_user_projects_owner_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plans',
            name='date_created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='projects',
            name='date_created',
            field=models.DateTimeField(),
        ),
    ]
