# Generated by Django 4.2.6 on 2023-11-28 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0007_table_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='number',
            field=models.CharField(max_length=255),
        ),
    ]