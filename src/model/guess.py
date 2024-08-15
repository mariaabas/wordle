from src.model import spot
from src.values import constants
from collections import Counter


def calculate_counts_secret_word(secret_word_letters_counts, letter):
    count = secret_word_letters_counts.get(letter)
    if count:
        secret_word_letters_counts.__setitem__(letter, count-1)


class GuessWord:

    def __init__(self, letters: str):
        self.letters = letters.upper()
        self.spots = []

    def compute_letters_in_spots(self, secret_word):
        secret_word_letters_counts = Counter(secret_word)
        for (index, letter) in enumerate(self.letters):
            letter_count = secret_word_letters_counts.get(letter)
            spot_result = spot.Spot(letter)
            spot_result.compute_status_letter_in_spot(secret_word, position_letter=index, letter_count=letter_count)
            calculate_counts_secret_word(secret_word_letters_counts, letter)
            self.spots.append(spot_result)

    def is_the_secret_word(self):
        for spot in self.spots:
            if spot.is_spot_in_correct_position():
                return False
        return True

    def is_correct_length(self):
        return len(self.letters) == constants.MAXIM_WORD_LENGTH

    def is_all_letters(self):
        return self.letters.isalpha()

    def is_valid_word(self, valid_words):
        return self.letters in valid_words