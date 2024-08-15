from enum import Enum


class LetterStatus(Enum):
    IN_SPOT = 1
    NOT_IN_SPOT = 2
    NOT_IN_WORD = 3
    INITIAL = 0
