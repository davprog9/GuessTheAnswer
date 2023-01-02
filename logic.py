from game_status import GameStatus


class Logic:

    def __init__(self, file_path, max_misses):
        self.file_path = file_path
        self.max_misses = max_misses
        self.game_status = GameStatus.IN_PROGRESS
        self.name = "John"




