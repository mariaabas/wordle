from src.model import game
from src.values import constants, messages
from src.helper import color
from src.enum import status_game
import emoji

if __name__ == '__main__':
    wordle_game = game.Game(constants.VALID_WORDS_FILE)
    print(emoji.emojize(messages.WELCOME_TO_THE_GAME))
    print(emoji.emojize(messages.PRESS_ANY_KEY))
    key_start_game = input()
    while wordle_game.guess_attempts <= constants.MAX_GUESS_ATTEMPS:
        print(emoji.emojize(messages.WRITE_A_WORD))
        guess_word = input()
        result = wordle_game.play(guess_word)
        if result.value:
            if result.status_game == status_game.StatusGame.WIN.value:
                print(emoji.emojize(messages.GUESS_ATTEMPTS.format(wordle_game.guess_attempts,
                                                     color.print_terminal_result(result.value))))
                wordle_game.guess_attempts = constants.MAX_GUESS_ATTEMPS + constants.INCREMENT_ONE_ROUND
                print(result.message)
            else:
                print(emoji.emojize(messages.GUESS_ATTEMPTS.format(wordle_game.guess_attempts,
                                                     color.print_terminal_result(result.value))))
                wordle_game.guess_attempts += constants.INCREMENT_ONE_ROUND
        else:
            print(result.message)
    print(messages.FINAL_RESULT_MESSAGE.format(wordle_game.secret_word))
