# Generated by Django 4.0.3 on 2022-04-23 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_alter_game_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='game_mode',
        ),
        migrations.AddField(
            model_name='game',
            name='game_mode',
            field=models.ManyToManyField(to='games.game_modes'),
        ),
    ]