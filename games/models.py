from django.db import models


class Game_Type(models.Model):
    FTP = 'First Person Shooter'
    TTP = 'Third Person Shooter'
    STRATEGY = 'Strategy'
    MMORPG = "MMORPG"
    RPG = 'RPG'
    RACING = 'Racing'
    SURVIVAL = 'Survival'

    Choice_make = [(FTP, 'First Person Shooter'),
                    (TTP, 'Third Person Shooter'),
                    (STRATEGY, 'Strategy'),
                    (MMORPG,'MMORPG'),
                    (RACING, 'Racing'),
                    (SURVIVAL, 'Survival')]

    type = models.CharField(
                    max_length=30,
                    choices=Choice_make,
                    default=None,
                    )

    objects = models.Manager()

    def __str__(self):
        return f'{self.type}'

    class Meta:
        verbose_name = 'Game Type'


class Game_Modes(models.Model):  

    Multiplayer = ' Multiplayer'
    Singleplayer = 'Singleplayer'
    Choice_make = [(Multiplayer, 'Multiplayer'),
                    (Singleplayer, 'Singleplayer')]

    mode = models.CharField(
                        max_length=30,
                        choices=Choice_make,
                        default=None)

    def __str__(self):
        return f'{self.mode}'

    class Meta:
        verbose_name = 'Game Mode'
    
    objects = models.Manager()

class Game(models.Model):
    """
        Fields and methods of the Game Type Class
    """
    objects = models.Manager()
    game_type = models.ForeignKey(Game_Type, on_delete=models.CASCADE,blank=True, null=True)
    game_mode = models.ManyToManyField(Game_Modes)
    shortcut = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    production_year = models.SmallIntegerField(default=None)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = "Title"

