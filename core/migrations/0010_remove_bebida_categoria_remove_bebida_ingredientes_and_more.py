# Generated by Django 5.1 on 2024-09-02 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_alter_itenscompra_compra"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bebida",
            name="categoria",
        ),
        migrations.RemoveField(
            model_name="bebida",
            name="ingredientes",
        ),
        migrations.RemoveField(
            model_name="itenscompra",
            name="comida",
        ),
        migrations.CreateModel(
            name="Produto",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                ("descrição", models.CharField(max_length=200)),
                ("preco", models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True)),
                ("quantidade", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "categoria",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="produtos",
                        to="core.categoria",
                    ),
                ),
                (
                    "ingredientes",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="produtos",
                        to="core.ingrediente",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="itenscompra",
            name="bebida",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="+", to="core.produto"),
        ),
        migrations.DeleteModel(
            name="Comida",
        ),
        migrations.DeleteModel(
            name="Bebida",
        ),
    ]
