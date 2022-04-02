from enum import Enum
from django.db import models

class Game(models.Model):

    """
    Nested Choice Class 
    """
    class Mode(Enum):
        singleplayer = (1, 'Mingleplayer')
        multiplayer = (2, 'Multiplayer')

        @classmethod
        def get_enum_value(cls, member):
            return member.value[0]

    """
    Class Fields
    """
    mode = models.CharField(max_length=15,
                            choices=[x.value for x in Mode],
                            default=Mode.get_enum_value(Mode.singleplayer)
                            )
    