# Generated by Django 2.0.8 on 2018-09-28 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_guest_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest_message',
            name='message',
            field=models.TextField(max_length=300, verbose_name='說啥'),
        ),
        migrations.AlterField(
            model_name='guest_message',
            name='replied_message',
            field=models.TextField(default='感謝您！', max_length=300, verbose_name='回覆啥'),
        ),
    ]
