
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0011_remove_game_modes_games_remove_game_game_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='game_type',
        ),
        migrations.AddField(
            model_name='game',
            name='game_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.game_type'),
        ),
    ]
