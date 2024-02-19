# Generated by Django 4.1.5 on 2024-02-09 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0002_alter_nodetypes_node_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodeslist',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='elements.nodetypes'),
        ),
        migrations.AlterField(
            model_name='nodetypes',
            name='node_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='nodetypes',
            name='node_type',
            field=models.IntegerField(choices=[(0, 'Activity'), (1, 'Milestone'), (2, 'Risk'), (3, 'Note'), (4, 'Test')], default=0),
        ),
    ]