# Generated by Django 4.1.3 on 2022-12-13 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reksadana', '0003_delete_treksadana_delete_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='TReksadana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('management', models.CharField(max_length=1000)),
                ('custodian', models.CharField(max_length=1000)),
                ('tipe_reksadana', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'Reksadana',
            },
        ),
    ]
