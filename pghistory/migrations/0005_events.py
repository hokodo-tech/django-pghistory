# Generated by Django 3.2.15 on 2022-09-15 01:09

from django.db import migrations, models
import django.db.models.manager

import pghistory.models


class Migration(migrations.Migration):

    dependencies = [
        ("pghistory", "0004_auto_20220906_1625"),
    ]

    operations = [
        migrations.CreateModel(
            name="Events",
            fields=[
                ("pgh_id", models.AutoField(primary_key=True, serialize=False)),
                ("pgh_created_at", models.DateTimeField(auto_now_add=True)),
                ("pgh_label", models.TextField(help_text="The event label.")),
                (
                    "pgh_table",
                    models.CharField(
                        help_text="The table under which the event is stored.", max_length=64
                    ),
                ),
                (
                    "pgh_data",
                    pghistory.models.PGHistoryJSONField(
                        help_text="The raw data of the event row."
                    ),
                ),
                (
                    "pgh_diff",
                    pghistory.models.PGHistoryJSONField(
                        help_text="The diff between the previous event and the current event."
                    ),
                ),
                (
                    "pgh_context_id",
                    models.UUIDField(help_text="The ID associated with the context.", null=True),
                ),
                (
                    "pgh_context",
                    models.JSONField(
                        help_text="The context associated with the event.",
                        null=True,
                        verbose_name="pghistory.Context",
                    ),
                ),
                (
                    "pgh_obj_table",
                    models.CharField(
                        help_text="The table under which the primary object is stored.",
                        max_length=64,
                    ),
                ),
                (
                    "pgh_obj_id",
                    models.TextField(help_text="The ID of the primary object.", null=True),
                ),
            ],
            options={
                "managed": False,
            },
            managers=[
                ("no_objects", django.db.models.manager.Manager()),
            ],
        ),
    ]
