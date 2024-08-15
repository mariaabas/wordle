import logging
logger = logging.getLogger(__name__)

class ReadFile(object):
    def __init__(self, filename):
        try:
            self.file = open(filename)
        except Error:
            logger.error("Error trying open the file: {}".format(Error))

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        try:
            self.file.close()
        except Error:
            logger.error("Error trying to close the file: {}".fomrat(Error))


def read_file_words(filename):
    with ReadFile(filename) as file:
        valid_words = [line.strip().upper() for line in file]
    return valid_words
