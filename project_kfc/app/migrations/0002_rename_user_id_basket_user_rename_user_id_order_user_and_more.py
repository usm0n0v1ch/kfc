# Generated by Django 4.2.16 on 2024-09-10 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='orderelement',
            old_name='order_id',
            new_name='order',
        ),
    ]
