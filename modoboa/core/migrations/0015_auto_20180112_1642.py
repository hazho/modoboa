# Generated by Django 1.11.8 on 2018-01-12 15:42
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_auto_20171010_1746"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="language",
            field=models.CharField(
                choices=[
                    ("cs", "\u010de\u0161tina"),
                    ("de", "deutsch"),
                    ("en", "english"),
                    ("el_GR", "\u03b5\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac"),
                    ("es", "espa\xf1ol"),
                    ("fr", "fran\xe7ais"),
                    ("it", "italiano"),
                    ("ja_JP", "\u65e5\u672c\u306e"),
                    ("nl", "nederlands"),
                    ("pt_PT", "portugu\xeas"),
                    ("pt_BR", "portugu\xeas (BR)"),
                    ("pl_PL", "polski"),
                    ("ru", "\u0440\u0443\u0441\u0441\u043a\u0438\u0439"),
                    ("sv", "svenska"),
                ],
                default="en",
                help_text="Prefered language to display pages.",
                max_length=10,
                verbose_name="language",
            ),
        ),
    ]
