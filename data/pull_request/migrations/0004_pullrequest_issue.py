# Generated by Django 5.2.1 on 2025-07-02 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("issue", "0007_issue_type"),
        ("pull_request", "0003_alter_pullrequest_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="pullrequest",
            name="issue",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="pull_requests",
                to="issue.issue",
            ),
        ),
    ]
