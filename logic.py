from game_status import GameStatus


class Logic:

    def __init__(self, file_path, max_misses):
        self.file_path = file_path
        self.max_misses = max_misses
        self.game_status = GameStatus.IN_PROGRESS
        self.counter = 0

    def file_opener(self):
        """Opens the file, and returns the file"""
        file = open(self.file_path, "r")
        return file

    def read_next_line(self, file):
        """
        Reads file's next line - by splitting it into a list of texts
        Each text contains either a question or an answer

        """
        next_line = file.readline().split(";")

        return next_line
