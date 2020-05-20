# Generated by Django 3.0.5 on 2020-05-15 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0004_auto_20200514_1249'),
        ('student', '0002_auto_20200504_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='group.Group'),
        ),
        migrations.AddField(
            model_name='student',
            name='telephone',
            field=models.CharField(default=None, max_length=20, null=True, unique=True),
        ),
    ]
