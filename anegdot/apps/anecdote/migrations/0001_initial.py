# Generated by Django 4.1 on 2022-11-27 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anecdote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anecdot_title', models.CharField(max_length=200, verbose_name="Ім'я гуморески")),
                ('anecdot_text', models.TextField(verbose_name='Текст гуморески')),
            ],
            options={
                'verbose_name': 'Анегдот',
                'verbose_name_plural': 'Анегдоти',
            },
        ),
    ]
