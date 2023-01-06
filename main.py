from logic import Logic

# Start point of the program

unit = Logic("venv/Questions.csv", 3)

print(f"Starting the game, you have maximum tries of {unit.max_misses}")
misses = unit.max_misses
while unit.max_misses > 0:

    end_of_file = unit.empty_line_check()
    if end_of_file == "Empty!":
        print(f"Congratulations you answered all questions, and you missed {misses - unit.max_misses} times!")
        break

    print(f"Next question is ` \n{unit.generate_question()}")

    answer = input("Yes or No ? ")
    result_for_answer = unit.user_answer(answer)

    if result_for_answer == "Out of tries!":
        print("You are out of tries!")

    elif result_for_answer == "Not the correct answer, please try again!":
        continue

