# Generated by Django 2.1.3 on 2018-12-18 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_auto_20181218_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelter',
            name='shelter_logo',
            field=models.ImageField(blank=True, null=True, upload_to='media/my_app'),
        ),
    ]
