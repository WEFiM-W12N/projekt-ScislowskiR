from enum import Enum
from django.db import models

class Game(models.Model):
    
    """
    Nested Choice Class 
    """
    class Game_Mode(Enum):
        singleplayer = (1, 'Singleplayer')
        multiplayer = (2, 'Multiplayer')

        @classmethod
        def get_enum_value(cls, member):
            return member.value[0]


    class Game_Type(Enum):
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
    Class Fields
    """
    title = models.CharField(max_length=50)
    production_year = models.SmallIntegerField(default=None)
    description = models.TextField(max_length=200)
    mode = models.IntegerField(
                            choices=[x.value for x in Game_Mode],
                            default=None)
    type = models.IntegerField(
                            choices=[x.value for x in Game_Type],
                            default=None
                            )

    def __str__(self):
        return self.title

