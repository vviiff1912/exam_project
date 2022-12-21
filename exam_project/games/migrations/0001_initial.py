# Generated by Django 3.2.16 on 2022-12-20 12:17

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('category', models.CharField(choices=[('ACTION', 'Action'), ('ADVENTURE', 'Adventure'), ('PUZZLE', 'Puzzle'), ('STRATEGY', 'Strategy'), ('SPORTS', 'Sports'), ('BOARD', 'Board/Card Game'), ('OTHER', 'Other')], max_length=9)),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(10)])),
                ('image_url', models.URLField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]