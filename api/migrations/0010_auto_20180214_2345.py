# Generated by Django 2.0.2 on 2018-02-15 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='company',
            field=models.CharField(max_length=100, verbose_name='Empresa'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='from_date',
            field=models.DateField(verbose_name='De'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='role',
            field=models.CharField(max_length=100, verbose_name='Cargo'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='to_date',
            field=models.DateField(verbose_name='Até'),
        ),
    ]