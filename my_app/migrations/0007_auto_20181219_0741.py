# Generated by Django 2.1.3 on 2018-12-19 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_auto_20181219_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelter',
            name='shelter_logo',
            field=models.ImageField(blank=True, null=True, upload_to='my_app/shelters'),
        ),
    ]