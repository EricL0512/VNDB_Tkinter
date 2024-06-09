from enum import Enum


class Tag(Enum):
    FANTASY = 'g1'
    DRAMA = 'g147'
    ROMANCE = 'g96'
    SEXUAL_CONTENT = 'g23'
    SCIENCE_FICTION = 'g105'
    COMEDY = 'g104'
    MYSTERY = 'g19'
    HORROR = 'g7'
    ACTION = 'g12'

print(Tag.FANTASY.value)