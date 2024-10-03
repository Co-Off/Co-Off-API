# Generated by Django 5.1.1 on 2024-09-30 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0019_ingrediente_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="cep",
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="cpf",
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="endereco",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="idade",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="telefone",
            field=models.DecimalField(blank=True, decimal_places=11, max_digits=11, null=True),
        ),
    ]