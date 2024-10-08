# Generated by Django 5.1.1 on 2024-10-01 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0020_user_cep_user_cpf_user_endereco_user_idade_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="cep",
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="cpf",
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="idade",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="telefone",
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
