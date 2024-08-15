import emoji


class ResultGame:
    def __init__(self, value, message, status_game):
        self.value = value
        self.message = emoji.emojize(message)
        self.status_game = status_game