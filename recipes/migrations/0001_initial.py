# Generated by Django 2.2.4 on 2019-10-08 22:39

import common.utils
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_measurement.models
import measurement.measures.energy
import measurement.measures.mass
import measurement.measures.volume


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('quantity', models.FloatField(default=0.0, null=True)),
                ('weight', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.mass.Mass, null=True)),
                ('volume', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('preparation_time', models.DurationField(default=datetime.timedelta)),
                ('cook_time', models.DurationField(default=datetime.timedelta)),
                ('servings', models.PositiveSmallIntegerField(default=1)),
                ('max_servings', models.PositiveIntegerField(default=1)),
                ('difficulty', models.SmallIntegerField(choices=[(1, 'easy'), (2, 'medium'), (3, 'hard')])),
                ('ingredients', models.ManyToManyField(related_name='in_recipes', to='recipes.Ingredient')),
                ('user', models.ForeignKey(on_delete=models.SET(common.utils.get_system_user), related_name='recipes', to=settings.AUTH_USER_MODEL)),
                ('users_who_made_this', models.ManyToManyField(related_name='made_recipes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('up', models.BooleanField(null=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'recipe')},
            },
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contents', models.TextField()),
                ('author', models.ForeignKey(on_delete=models.SET(common.utils.get_system_user), related_name='tips', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('number', models.PositiveSmallIntegerField()),
                ('directions', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='recipes.Recipe')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='votes',
            field=models.ManyToManyField(related_name='voted_recipes', through='recipes.Vote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('calories', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.energy.Energy)),
                ('total_fat', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('saturated_fat', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('cholesterol', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('sodium', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('potassium', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('carbohydrates', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('fiber', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('sugar', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('protein', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('vitamin_a', models.FloatField(default=0.0)),
                ('vitamin_c', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('calcium', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('iron', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('vitamin_d', models.FloatField(default=0.0)),
                ('vitamin_e', models.FloatField(default=0.0)),
                ('vitamin_k', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('thiamin', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('riboflavin', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('niacin', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('vitamin_b6', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('folate', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('vitamin_b12', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('biotin', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('pantothenic_acid', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('phosphorus', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('iodine', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('magnesium', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('zinc', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('selenium', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('copper', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('manganese', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('chromium', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('molybdenum', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('chloride', django_measurement.models.MeasurementField(default=0, measurement=measurement.measures.volume.Volume)),
                ('recipe', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
