# Generated by Django 4.2.11 on 2024-04-22 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='equipment',
            name='model',
            field=models.CharField(default='01', max_length=255),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='serial_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
