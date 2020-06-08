# Generated by Django 2.2.6 on 2020-05-20 07:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_audit', '0004_remove_file_filext'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='filext',
            field=models.FileField(default='', upload_to='%Y/%m/%d', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'], message='必须是图像文件')]),
        ),
    ]