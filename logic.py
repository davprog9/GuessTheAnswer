from game_status import GameStatus
from question import Question


class Logic:

    def __init__(self, file_path: str, max_misses: int):
        self.file_path = file_path
        self.max_misses = max_misses
        self.__game_status = GameStatus.IN_PROGRESS
        self.counter = 0
        self.questions = []
        self.fill_in_questions(file_path, self.questions)

    @property
    def game_status(self) -> GameStatus:
        """
        Returns the game status from game_status.py
        :return: Game status
        """

        return self.__game_status

    def fill_in_questions(self, file_path, questions):
        with open(file_path, encoding="utf8") as file:
            for line in file:
                q = self.parse_line(line)
                questions.append(q)

    def parse_line(self, line) -> Question:
        parts = line.split(";")
        text = parts[0]
        is_correct = parts[1]
        explanation = parts[2]

        return Question(text, is_correct, explanation)

    def generate_question(self) -> str:
        """
        Picks a question from question list and uses
        counter as a question counter
        :return: Question from questions list
        """

        return self.questions[self.counter].text

    def user_answer(self, answer_input):
        """
        Accepts answer_input as an argument, which is a user provided answer
        for a question. Capitalizes the user provided answer, then check if it matches to
        the answer we have in the csv file.

        :return: "Out of tries!" if maximum tries are <= 0 otherwise prints "Not the correct answer, please try again!"
        """

        capitalized_answer = answer_input.capitalize()

        if capitalized_answer == self.questions[self.counter].is_true:
            print(f"You've guessed the correct answer!\n{self.questions[self.counter].explanation}")
            self.counter += 1

        else:
            self.max_misses -= 1
            self.__game_status = GameStatus.LOST if self.max_misses <= 0 else GameStatus.IN_PROGRESS

            if self.__game_status == GameStatus.IN_PROGRESS:
                print("Oops, wrong answer, try again!")
                return "Wrong answer"
            
            elif self.__game_status == GameStatus.LOST:
                print("Oops, wrong answer, you are out of tries, game over!")

    def empty_line_check(self):
        if self.counter > len(self.questions) - 1:
            print("No more questions left, you won!")
            self.__game_status = GameStatus.WON
