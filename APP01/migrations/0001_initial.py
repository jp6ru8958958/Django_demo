# Generated by Django 2.2.1 on 2019-05-29 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hello_models',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Column1', models.TextField(default='Column1_df')),
                ('Column2', models.TextField(default='Column2_df')),
                ('Column3', models.DateTimeField(auto_now=True)),
                ('Column4', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'APP01',
            },
        ),
    ]
