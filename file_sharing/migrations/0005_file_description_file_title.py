# Generated by Django 4.2.8 on 2024-01-05 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("file_sharing", "0004_alter_user_is_active_alter_user_is_staff"),
    ]

    operations = [
        migrations.AddField(
            model_name="file",
            name="description",
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name="file",
            name="title",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
