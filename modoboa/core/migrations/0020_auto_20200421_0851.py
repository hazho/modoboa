# Generated by Django 2.2.9 on 2020-04-21 06:51

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0019_auto_20200121_1659"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                max_length=128,
                null=True,
                region=None,
                verbose_name="Phone number",
            ),
        ),
    ]
