# Generated by Django 4.2.6 on 2023-10-23 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_rename_flash_card_flashcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlashPacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='flashcard',
            name='profile',
        ),
        migrations.AddField(
            model_name='flashcard',
            name='rating',
            field=models.IntegerField(default=5),
        ),
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.AddField(
            model_name='flashpacks',
            name='cards',
            field=models.ManyToManyField(to='base.flashcard'),
        ),
    ]