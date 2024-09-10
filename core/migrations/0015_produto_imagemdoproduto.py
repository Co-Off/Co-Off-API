# Generated by Django 5.1.1 on 2024-09-10 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_alter_produto_ingredientes"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="produto",
            name="imagemDoProduto",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="uploader.image",
            ),
        ),
    ]
