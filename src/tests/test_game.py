from unittest import TestCase
from src.model import game
from src.enum import status_game, letter_status
from src.values import messages
import emoji

VALID_WORD_TEST_FILE_TXT = 'files/valid_word_test.txt'
SECRET_WORD = 'hello'


class GameTest(TestCase):
    def setUp(self):
        self.world_game_test = game.Game(VALID_WORD_TEST_FILE_TXT)
        # Force to get one specific word from the valid_word for test
        self.world_game_test.secret_word = SECRET_WORD.upper()

    def test_guess_word_is_empty(self):
        guess_word_test = ''
        result_wordle_text = self.world_game_test.play(guess_word_test)
        self.assertIsNone(result_wordle_text.value)
        self.assertEqual(status_game.StatusGame.PLAYING.value, result_wordle_text.status_game)
        self.assertEqual(emoji.emojize(messages.ERROR_LENGTH_WORD), result_wordle_text.message)

    def test_guess_word_incorrect_length(self):
        guess_word_test = 'tonight'
        result_wordle_text = self.world_game_test.play(guess_word_test)
        self.assertIsNone(result_wordle_text.value)
        self.assertEqual(status_game.StatusGame.PLAYING.value, result_wordle_text.status_game)
        self.assertEqual(emoji.emojize(messages.ERROR_LENGTH_WORD),result_wordle_text.message)

    def test_guess_word_is_not_all_letters(self):
        guess_word_test = 'he78o'
        result_wordle_text = self.world_game_test.play(guess_word_test)
        self.assertIsNone(result_wordle_text.value)
        self.assertEqual(status_game.StatusGame.PLAYING.value, result_wordle_text.status_game)
        self.assertEqual(emoji.emojize(messages.ERROR_NUMBERS_ON_WORD), result_wordle_text.message)

    def test_guess_word_is_not_a_valid_word(self):
        guess_word_test = 'input'
        result_wordle_text = self.world_game_test.play(guess_word_test)
        self.assertIsNone(result_wordle_text.value)
        self.assertEqual(status_game.StatusGame.PLAYING.value, result_wordle_text.status_game)
        self.assertEqual(emoji.emojize(messages.ERROR_INVALID_WORD), result_wordle_text.message)

    def test_guess_word_is_valid_word_but_any_letter_is_on_the_secret_word(self):
        guess_word_text = 'draft'
        result_wordle_text = self.world_game_test.play(guess_word_text)

        # Check letters word result
        self.assertEqual(letter_status.LetterStatus.NOT_IN_WORD.value, result_wordle_text.value[0].status)
        self.assertEqual(letter_status.LetterStatus.NOT_IN_WORD.value, result_wordle_text.value[1].status)
        self.assertEqual(letter_status.LetterStatus.NOT_IN_WORD.value, result_wordle_text.value[2].status)
        self.assertEqual(letter_status.LetterStatus.NOT_IN_WORD.value, result_wordle_text.value[3].status)
        self.assertEqual(letter_status.LetterStatus.NOT_IN_WORD.value, result_wordle_text.value[4].status)

        self.assertEqual(result_wordle_text.status_game, status_game.StatusGame.PLAYING.value)

    def test_guess_word_is_valid_word_and_one_letter_is_on_the_secret_word_but_not_in_the_spot(self):
        guess_word_text = 'about'
        result_wordle_text = self.world_game_test.play(guess_word_text)

        # Check letters word result
        self.assertEqual(letter_status.LetterStatus.NOT_IN_WORD.value, result_wordle_text.value[0].status)
        self.assertEqual(letter_status.LetterStatus.NOT_IN_WORD.value, result_wordle_text.value[1].status)
        self.assertEqual(letter_status.LetterStatus.NOT_IN_SPOT.value, result_wordle_text.value[2].status)
        self.assertEqual(letter_status.LetterStatus.NOT_IN_WORD.value, result_wordle_text.value[3].status)
        self.assertEqual(letter_status.LetterStatus.NOT_IN_WORD.value, result_wordle_text.value[4].status)

        self.assertEqual(status_game.StatusGame.PLAYING.value, result_wordle_text.status_game)

    def test_guess_word_is_valid_word_and_one_letter_is_on_the_secret_word_and_into_the_spot(self):
        guess_word_text = 'ratio'

        result_wordle_text = self.world_game_test.play(guess_word_text)

        # Check letters word result
        self.assertEqual(letter_status.LetterStatus.NOT_IN_WORD.value, result_wordle_text.value[0].status)
        self.assertEqual(letter_status.LetterStatus.NOT_IN_WORD.value, result_wordle_text.value[1].status)
        self.assertEqual(letter_status.LetterStatus.NOT_IN_WORD.value, result_wordle_text.value[2].status)
        self.assertEqual(letter_status.LetterStatus.NOT_IN_WORD.value, result_wordle_text.value[3].status)
        self.assertEqual(letter_status.LetterStatus.IN_SPOT.value, result_wordle_text.value[4].status)

        self.assertEqual(status_game.StatusGame.PLAYING.value, result_wordle_text.status_game)

    def test_guess_word_is_valid_word_and_there_are_two_duplicate_letters_but_only_one_is_on_the_secret_word_and_into_the_spot(
            self):
        guess_word_text = 'peter'

        result_wordle_text = self.world_game_test.play(guess_word_text)

        # Check letters word result
        self.assertEqual(letter_status.LetterStatus.NOT_IN_WORD.value, result_wordle_text.value[0].status)
        self.assertEqual(letter_status.LetterStatus.IN_SPOT.value, result_wordle_text.value[1].status)
        self.assertEqual(letter_status.LetterStatus.NOT_IN_WORD.value, result_wordle_text.value[2].status)
        self.assertEqual(letter_status.LetterStatus.NOT_IN_WORD.value, result_wordle_text.value[3].status)
        self.assertEqual(letter_status.LetterStatus.NOT_IN_WORD.value, result_wordle_text.value[4].status)

        self.assertEqual(status_game.StatusGame.PLAYING.value, result_wordle_text.status_game)

    def test_guess_word_is_valid_word_and_there_are_two_duplicate_letters_but_only_one_is_on_the_secret_word_and_not_into_the_spot(
            self):
        guess_word_text = 'blood'

        result_wordle_text = self.world_game_test.play(guess_word_text)

        # Check letters word result
        self.assertEqual(letter_status.LetterStatus.NOT_IN_WORD.value, result_wordle_text.value[0].status)
        self.assertEqual(letter_status.LetterStatus.NOT_IN_SPOT.value, result_wordle_text.value[1].status)
        self.assertEqual(letter_status.LetterStatus.NOT_IN_SPOT.value, result_wordle_text.value[2].status)
        self.assertEqual(letter_status.LetterStatus.NOT_IN_WORD.value, result_wordle_text.value[3].status)
        self.assertEqual(letter_status.LetterStatus.NOT_IN_WORD.value, result_wordle_text.value[4].status)

        self.assertEqual(status_game.StatusGame.PLAYING.value, result_wordle_text.status_game)

    def test_guess_word_is_valid_word_and_all_letters_are_into_the_spot(
            self):
        guess_word_text = 'hello'

        result_wordle_text = self.world_game_test.play(guess_word_text)

        # Check letters word result
        self.assertEqual(letter_status.LetterStatus.IN_SPOT.value, result_wordle_text.value[0].status)
        self.assertEqual(letter_status.LetterStatus.IN_SPOT.value, result_wordle_text.value[1].status)
        self.assertEqual(letter_status.LetterStatus.IN_SPOT.value, result_wordle_text.value[2].status)
        self.assertEqual(letter_status.LetterStatus.IN_SPOT.value, result_wordle_text.value[3].status)
        self.assertEqual(letter_status.LetterStatus.IN_SPOT.value, result_wordle_text.value[4].status)

        self.assertEqual(status_game.StatusGame.WIN.value, result_wordle_text.status_game)