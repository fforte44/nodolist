# Generated by Django 4.0 on 2022-07-31 03:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('nodolist', '0004_alter_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
