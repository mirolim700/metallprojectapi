# Generated by Django 4.1.7 on 2023-04-02 05:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_alter_infomodel_bot_username_alter_usersmodel_lang'),
    ]

    operations = [
        migrations.AddField(
            model_name='infomodel',
            name='location',
            field=models.TextField(default=datetime.datetime(2023, 4, 2, 5, 39, 56, 909019, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usersmodel',
            name='lang',
            field=models.CharField(default='uz', max_length=2),
        ),
        migrations.AlterField(
            model_name='usersmodel',
            name='username',
            field=models.TextField(null=True),
        ),
    ]
