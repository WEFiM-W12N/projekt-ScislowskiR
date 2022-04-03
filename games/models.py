from enum import Enum
from django.db import models


class Game_Type(models.Model):
    """
        Nested Enum Class to display available choices of Game Type 
    """
    class Game_Type_Enum(Enum):
        FTP = (1, 'First Person Shooter')
        TTP = (2, 'Third Person Shooter')
        strategy = (3, 'Strategy')
        MMORPG = (4, "MMORPG")
        RPG = (5, 'RPG')
        racing = (6, 'Racing')
        survival = (7, 'Survival')

        @classmethod
        def get_enum_value(cls, member):
            return member.value[0]
    """
        Fields and methods of the Game Type Class
    """

    type = models.IntegerField(
                    choices=[x.value for x in Game_Type_Enum],
                    default=None
                    )

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Game Type"

class Game_Modes(models.Model):  
    """
        Nested Enum Class to display available choices of Game Type 
    """
    class Game_Modes_Enum(Enum):
        singleplayer = (1, 'Singleplayer')
        multiplayer = (2, 'Multiplayer')

        @classmethod
        def get_enum_value(cls, member):
            return member.value[0]

    """
        Fields and methods of the Game Type Class
    """  
    mode = models.IntegerField(
                        choices=[x.value for x in Game_Modes_Enum],
                        default=None)


    def __str__(self):
        return self.mode
    
    class Meta:
        verbose_name = "Game Mode"

class Game(models.Model):
    """
        Fields and methods of the Game Type Class
    """
    game_type = models.ForeignKey(Game_Type, on_delete=models.CASCADE,blank=True, null=True)
    game_mode = models.ForeignKey(Game_Modes, on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=50)
    production_year = models.SmallIntegerField(default=None)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Title"

