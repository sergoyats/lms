# Generated by Django 3.0.5 on 2020-05-14 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20200512_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='telephone',
            field=models.CharField(default=380966666666, max_length=20, unique=True),
        ),
    ]
