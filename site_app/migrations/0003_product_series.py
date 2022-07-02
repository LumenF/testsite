# Generated by Django 4.0.3 on 2022-07-01 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0002_group_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='site_app.series', verbose_name='Серия'),
            preserve_default=False,
        ),
    ]
