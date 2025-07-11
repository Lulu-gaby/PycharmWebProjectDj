# Generated by Django 5.2.3 on 2025-07-07 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Films_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название фильма')),
                ('description', models.CharField(max_length=200, verbose_name='Описание описание')),
                ('comments', models.TextField(verbose_name='Отзывы о фильме')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]
