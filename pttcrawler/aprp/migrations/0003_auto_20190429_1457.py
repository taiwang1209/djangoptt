# Generated by Django 2.2 on 2019-04-29 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aprp', '0002_auto_20190426_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailytran',
            name='name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='dailytrans', to='aprp.Product'),
        ),
    ]
