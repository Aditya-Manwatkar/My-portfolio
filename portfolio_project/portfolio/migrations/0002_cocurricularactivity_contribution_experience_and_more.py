# Generated by Django 5.1.4 on 2024-12-28 04:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CocurricularActivity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Contribution",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("url", models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company", models.CharField(max_length=100)),
                ("position", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Internship",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company", models.CharField(max_length=100)),
                ("position", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="ResearchBlog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("publication_date", models.DateField()),
                ("url", models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="SocialProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "platform",
                    models.CharField(
                        choices=[
                            ("LI", "LinkedIn"),
                            ("GH", "GitHub"),
                            ("TW", "Twitter"),
                            ("FB", "Facebook"),
                            ("IG", "Instagram"),
                            ("OT", "Other"),
                        ],
                        max_length=2,
                    ),
                ),
                ("url", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Thought",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
