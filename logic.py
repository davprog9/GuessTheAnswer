from game_status import GameStatus
from question import Question

class Logic:

    def __init__(self, file_path, max_misses):
        self.file_path = file_path
        self.max_misses = max_misses
        self.__game_status = GameStatus.IN_PROGRESS
        self.counter = 0
        self.questions = []
        self.fill_in_questions(file_path, self.questions)

    @property
    def game_status(self):
        return self.game_status

    def fill_in_questions(self, file_path, questions):
        with open(file_path, encoding="utf8") as file:
            for line in file:
                q = self.parse_line(line)
                questions.append(q)

    def parse_line(self, line):
        parts = line.split(";")
        text = parts[0]
        is_correct = parts[1]
        explanation = parts[2]

        return Question(text, is_correct, explanation)




