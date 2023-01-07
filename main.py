from logic import Logic
from game_status import GameStatus

# Start point of the client file
allowed_max_tries = int(input("Please provide allowed maximum tries from 1 to 5 "))
unit = Logic("venv/Questions.csv", allowed_max_tries)

print(f"Starting the game, you have maximum tries of {unit.max_misses}")
misses = unit.max_misses
while unit.game_status == GameStatus.IN_PROGRESS:

    if unit.game_status == GameStatus.WON:
        print(f"Congratulations you answered all questions, and you missed {misses - unit.max_misses} times!")

    print(f"Do you believe the below statement [Yes/No] \n{unit.generate_question()}")

    answer = input()
    result_for_answer = unit.user_answer(answer)

    if result_for_answer == "Wrong answer":
        continue

    unit.empty_line_check()
