# Generated by Django 3.2.13 on 2022-10-12 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0022_user_tfa_enabled"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="language",
            field=models.CharField(
                choices=[
                    ("br", "breton"),
                    ("cs", "čeština"),
                    ("de", "deutsch"),
                    ("en", "english"),
                    ("el", "ελληνικά"),
                    ("es", "español"),
                    ("fr", "français"),
                    ("it", "italiano"),
                    ("ja", "日本の"),
                    ("nl", "nederlands"),
                    ("pt", "português"),
                    ("pt-br", "português (BR)"),
                    ("pl", "polski"),
                    ("ro", "Română"),
                    ("ru", "русский"),
                    ("sv", "svenska"),
                    ("tr", "türk"),
                    ("zh-hant", "中文（台灣）"),
                ],
                default="en",
                help_text="Prefered language to display pages.",
                max_length=10,
                verbose_name="language",
            ),
        ),
    ]
