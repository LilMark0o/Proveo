# Generated by Django 5.0.4 on 2024-05-04 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_producto_ultimopedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_registro',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='ultimoPedido',
            field=models.DateField(),
        ),
    ]
