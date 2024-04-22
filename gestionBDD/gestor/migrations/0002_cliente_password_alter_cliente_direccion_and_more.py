# Generated by Django 5.0.3 on 2024-04-01 16:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gestor", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cliente",
            name="password",
            field=models.CharField(default="nulo", max_length=15),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="direccion",
            field=models.CharField(default="nulo", max_length=50),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="email",
            field=models.EmailField(default="nulo", max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="nombre",
            field=models.CharField(default="nulo", max_length=30),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="telefono",
            field=models.CharField(default="nulo", max_length=10),
        ),
    ]
