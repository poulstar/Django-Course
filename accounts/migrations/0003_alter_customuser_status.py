# Generated by Django 4.0.5 on 2023-04-10 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_customuser_age_customuser_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.SmallIntegerField(blank=True, default=1, null=True),
        ),
    ]
