# Generated by Django 3.0.2 on 2020-04-02 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20200316_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='ubigeo',
            field=models.CharField(blank=True, max_length=6, verbose_name='ubigeo'),
        ),
    ]