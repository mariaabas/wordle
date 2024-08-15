def in_spot(letter: str):
    return f"\033[1m\033[42m\033[30m{letter.upper()}\033[0m"


def not_in_spot(letter: str):
    return f"\033[1m\033[43m\033[30m{letter.upper()}\033[0m"


def not_in_word(letter: str):
    return f"\033[1m\033[47m\033[30m{letter.upper()}\033[0m"


def print_terminal_result(spots):
    colors_letters = ''
    for spot in spots:
        if spot.is_in_spot():
            color_letter = in_spot(letter=spot.letter)
            colors_letters += color_letter
        elif spot.is_not_in_spot():
            color_letter = not_in_spot(letter=spot.letter)
            colors_letters += color_letter
        elif spot.is_not_in_word():
            color_letter = not_in_word(letter=spot.letter)
            colors_letters += color_letter
    return colors_letters
