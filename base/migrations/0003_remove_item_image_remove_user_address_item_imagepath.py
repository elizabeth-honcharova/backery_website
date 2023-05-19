# Generated by Django 4.1.7 on 2023-05-18 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_user_address_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.AddField(
            model_name='item',
            name='imagePath',
            field=models.CharField(default='f1.svg', max_length=200),
        ),
    ]
