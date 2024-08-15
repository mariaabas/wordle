from src.enum import letter_status


class Spot:
    def __init__(self, letter: chr):
        self.letter = letter
        self.status = letter_status.LetterStatus.INITIAL.value

    def compute_status_letter_in_spot(self, secret_word, position_letter, letter_count):
        if self.letter == secret_word[position_letter]:
            self.status = letter_status.LetterStatus.IN_SPOT.value
        elif self.letter in secret_word:
            if letter_count <= 0:
                self.status = letter_status.LetterStatus.NOT_IN_WORD.value
            else:
                self.status = letter_status.LetterStatus.NOT_IN_SPOT.value
        else:
            self.status = letter_status.LetterStatus.NOT_IN_WORD.value

    def is_in_spot(self):
        return self.status == letter_status.LetterStatus.IN_SPOT.value

    def is_not_in_spot(self):
        return self.status == letter_status.LetterStatus.NOT_IN_SPOT.value

    def is_not_in_word(self):
        return self.status == letter_status.LetterStatus.NOT_IN_WORD.value

    def is_spot_in_correct_position(self):
        return self.is_not_in_spot() or self.is_not_in_word()