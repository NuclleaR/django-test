# Generated by Django 2.1 on 2018-08-12 22:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('object_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('image_url', models.ImageField(blank=True, default=None, upload_to='media/')),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AchievementUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('achievement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='achievements.Achievement', to_field='object_id')),
            ],
        ),
    ]
