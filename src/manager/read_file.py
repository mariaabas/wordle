import logging
logger = logging.getLogger(__name__)

class FileOpenError(Exception):
    """Custom exception for file open errors."""
    pass

class ReadFile(object):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
        except FileNotFoundError:
            logger.error(f"Error: The file '{self.filename}' was not found.")
            raise FileOpenError(f"Error: The file '{self.filename}' was not found.")
        except IOError:
            logger.error(f"Error: An IO error occurred while trying to open '{self.filename}'.")
            raise FileOpenError(f"Error: An IO error occurred while trying to open '{self.filename}'.")
        except Exception as exception:
            logger.error(f"An unexpected error occurred: {exception}")
            raise FileOpenError(f"An unexpected error occurred: {exception}")
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        if self.file:
            self.file.close()


def read_file_words(filename):
    try:
        with ReadFile(filename) as file:
            valid_words = [line.strip().upper() for line in file]
        return valid_words
    except FileOpenError as file_open_error:
        logger.error(f"An unexpected error occurred: {file_open_error}")

