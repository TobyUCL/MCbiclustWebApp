# Generated by Django 2.0 on 2018-02-20 21:20

from django.db import migrations, models
import mcbiclustweb.models


class Migration(migrations.Migration):

    dependencies = [
        ('mcbiclustweb', '0003_auto_20180205_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='gem',
            field=models.FileField(upload_to=mcbiclustweb.models.user_directory_path),
        ),
    ]