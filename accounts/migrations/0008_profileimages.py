# Generated by Django 4.1.5 on 2024-02-16 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_rename_user_id_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(upload_to='accounts/user_images')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='accounts.profile')),
            ],
        ),
    ]
