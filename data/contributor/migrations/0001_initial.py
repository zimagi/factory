# Generated by Django 5.2.1 on 2025-06-22 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contributor",
            fields=[
                ("created", models.DateTimeField(editable=False, null=True)),
                ("updated", models.DateTimeField(editable=False, null=True)),
                (
                    "id",
                    models.CharField(
                        editable=False, max_length=64, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("provider", models.CharField(default=None, max_length=256, null=True)),
                ("url", models.URLField(default=None, max_length=256, null=True)),
            ],
            options={
                "verbose_name": "contributor",
                "verbose_name_plural": "contributors",
                "db_table": "factory_contributor",
                "ordering": ["id"],
                "abstract": False,
                "unique_together": {("provider", "name")},
            },
        ),
    ]
