# Generated by Django 4.1.3 on 2022-12-08 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vahak_api', '0002_routes_user_userprofile_delete_usermodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routes',
            name='name',
        ),
        migrations.AddField(
            model_name='routes',
            name='name',
            field=models.ManyToManyField(blank=True, related_name='authors', to='vahak_api.user'),
        ),
    ]
