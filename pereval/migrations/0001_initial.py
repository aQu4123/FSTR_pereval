# Generated by Django 5.1.6 on 2025-05-21 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('height', models.FloatField(verbose_name='Высота')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(blank=True, max_length=5, verbose_name='Уровень сложности зимой')),
                ('summer', models.CharField(blank=True, max_length=5, verbose_name='Уровень сложности летом')),
                ('autumn', models.CharField(blank=True, max_length=5, verbose_name='Уровень сложности осенью')),
                ('spring', models.CharField(blank=True, max_length=5, verbose_name='Уровень сложности весной')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('phone', models.CharField(max_length=15, verbose_name='Телефонный номер')),
                ('fam', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('otc', models.CharField(blank=True, max_length=100, verbose_name='Отчество')),
            ],
        ),
        migrations.CreateModel(
            name='Added',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('new', 'Новая'), ('pending', 'На модерации'), ('accepted', 'Принята'), ('rejected', 'Отклонена')], default='new', max_length=15)),
                ('beautyTitle', models.CharField(max_length=100, verbose_name='Тип местности')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('other_titles', models.CharField(max_length=100, verbose_name='Другие названия')),
                ('connect', models.TextField(blank=True, verbose_name='Сопроводительный текст')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('coords', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pereval.coords')),
                ('level', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pereval.level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.user')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.URLField()),
                ('title', models.CharField(max_length=100)),
                ('pereval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pereval.added')),
            ],
        ),
    ]
