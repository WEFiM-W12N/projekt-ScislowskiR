from enum import Enum
from re import M
from django.db import models


class Game_Type(models.Model):
    """
        Nested Enum Class to display available choices of Game Type 
    """



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
    """
        Fields and methods of the Game Type Class
    """

    type = models.CharField(
                    max_length=30,
                    choices=Choice_make,
                    default=None,
                    )

    def __str__(self):
        return self.get_type_display()

    class Meta:
        verbose_name = 'Game Type'


class Game_Modes(models.Model):  
    """
        Nested Enum Class to display available choices of Game Type 
    """
    Multiplayer = ' MP'
    Singleplayer = 'SP'
    Choice_make = [(Multiplayer, 'Multiplayer'),
                    (Singleplayer, 'Singleplayer')]

    """
        Fields and methods of the Game Type Class
    """  
    mode = models.CharField(
                        max_length=30,
                        choices=Choice_make,
                        default=None)

    def __str__(self):
        return self.get_mode_display()

    class Meta:
        verbose_name = 'Game Mode'
    


class Game(models.Model):
    """
        Fields and methods of the Game Type Class
    """
    game_type = models.ForeignKey(Game_Type, on_delete=models.CASCADE,blank=True, null=True)
    game_mode = models.ForeignKey(Game_Modes, on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=50)
    production_year = models.SmallIntegerField(default=None)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Title"

