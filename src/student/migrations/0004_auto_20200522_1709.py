# Generated by Django 3.0.5 on 2020-05-22 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0005_auto_20200522_1709'),
        ('student', '0003_auto_20200515_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(db_index=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='group.Group'),
        ),
    ]
