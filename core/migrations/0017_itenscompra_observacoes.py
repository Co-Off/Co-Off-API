# Generated by Django 5.1.1 on 2024-09-27 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0016_itenscompra_produto_alter_itenscompra_compra"),
    ]

    operations = [
        migrations.AddField(
            model_name="itenscompra",
            name="observacoes",
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
