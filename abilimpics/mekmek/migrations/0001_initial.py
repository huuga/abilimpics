# Generated by Django 4.0.4 on 2022-05-13 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('date_of_birth', models.CharField(max_length=10, verbose_name='Дата рождения')),
                ('disease', models.CharField(max_length=50, verbose_name='Заболевание')),
                ('studying_now', models.CharField(max_length=5, verbose_name='Обучается в данное время')),
                ('graduate', models.CharField(max_length=20, verbose_name='Уровень образования')),
                ('graduate_year', models.CharField(max_length=5, verbose_name='Планируемый год окончания образовательной организации')),
            ],
        ),
    ]
