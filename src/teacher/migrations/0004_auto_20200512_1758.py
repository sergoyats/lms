# Generated by Django 3.0.5 on 2020-05-12 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_auto_20200508_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='telephone',
            field=models.CharField(default=380966666666, max_length=20),
        ),
    ]
