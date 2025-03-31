# Generated by Django 5.1.7 on 2025-03-15 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.CharField(max_length=500)),
                ('data', models.DateTimeField()),
                ('local', models.CharField(max_length=250)),
                ('categoria', models.CharField(choices=[('Música', 'Música'), ('Teatro', 'Teatro'), ('Cinema', 'Cinema'), ('Arte', 'Arte')], max_length=7)),
            ],
        ),
    ]
