from src.manager import read_file
from src.model import guess, result
from src.values import messages
from src.enum import status_game
import random


class Game:

    def __init__(self, filename: str):
        self.valid_words = read_file.read_file_words(filename)
        self.secret_word = random.choice(self.valid_words)
        self.guess_attempts = 1

    def play(self, input_guess_word):
        guess_word = guess.GuessWord(input_guess_word)
        if guess_word.is_correct_length():
            if guess_word.is_all_letters():
                if guess_word.is_valid_word(self.valid_words):
                    guess_word.compute_letters_in_spots(secret_word=self.secret_word)
                    if guess_word.is_the_secret_word():
                        return result.ResultGame(value=guess_word.spots,
                                                 message=messages.WIN_GAME_MESSAGE,
                                                 status_game=status_game.StatusGame.WIN.value)

                    return result.ResultGame(value=guess_word.spots,
                                             message='',
                                             status_game=status_game.StatusGame.PLAYING.value)

                return result.ResultGame(value=None,
                                         message=messages.ERROR_INVALID_WORD,
                                         status_game=status_game.StatusGame.PLAYING.value)

            return result.ResultGame(value=None, message=messages.ERROR_NUMBERS_ON_WORD,
                                     status_game=status_game.StatusGame.PLAYING.value)

        return result.ResultGame(value=None, message=messages.ERROR_LENGTH_WORD,
                                 status_game=status_game.StatusGame.PLAYING.value)
