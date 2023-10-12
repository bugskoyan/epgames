# Generated by Django 4.2.6 on 2023-10-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='posters', verbose_name='постер'),
        ),
        migrations.AlterField(
            model_name='game',
            name='rate',
            field=models.FloatField(default=3, max_length=5, verbose_name='рейтинг'),
        ),
    ]
