from questions_for_quiz import questions  # Import questions from questions_for_quiz.py
import random

def filter_by_topic(questions):
    # Get user to select a topic
    valid_choices = ['muay thai', 'ufc', 'boxing']
    player_choice = input("Type in a Topic: Muay Thai, Ufc, Boxing: ").strip()
    while player_choice.lower() not in valid_choices:
        player_choice = input("Invalid choice. Please select a valid topic: Muay Thai, Ufc, Boxing: ").strip()

    filtered_questions = [question for question in questions if question["Topic"].lower() == player_choice.lower()]
    return filtered_questions

def how_many_questions():
    user_questions = int(input("How many questions would you like to answer? "))
    return user_questions

def ask_questions(score, qascore, filtered_questions, user_questions):
    hint_limit = 3
    hint_count = 0

    for i, question in enumerate(filtered_questions[:user_questions]):
        print(f"Question {i + 1}: {question['Question']}")
        for idx, option in enumerate(question["Options"], start=1):
            print(f"{idx}. {option}")

        while True:
            user_answer = input("Your answer (type the option number, text, or 'hint'): ").strip()

            if user_answer.lower() == "hint":
                if hint_count < hint_limit:
                    print(f"Hint: {question['Hint']}")
                    hint_count += 1
                    print(f"You have used {hint_count} out of {hint_limit} hints.")
                else:
                    print("You have used all your hints. No more hints available.")
            else:
                if user_answer.isdigit() and int(user_answer) in range(1, len(question["Options"]) + 1):
                    selected_option = question["Options"][int(user_answer) - 1]
                else:
                    selected_option = user_answer

                if selected_option.lower() == question["Answer"].lower():
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The correct answer is {question['Answer']}.")
                qascore += 1
                break

    return score, qascore

def welcome_to_the_quiz():
    print("Welcome to Tom Kirby's quiz!!!")

def average_score(score, qascore):
    if qascore == 0:
        print("No questions were answered.")
        return 0
    else:
        print(f"You got {score} out of {qascore} questions correct.")
        avg = score / qascore * 100
        print(f"Your average score is {avg:.2f}%")
        return avg

def play_again_or_end():
    play_again = input("Do you want to play again? (yes/no): ").strip()
    if play_again.lower() in ['y', 'yes']:
        main_without_welcome_page()  # Call the function without the welcome page
    else:
        print("Thank you for playing the quiz. Goodbye!")
        exit()

def main():
    score = 0
    qascore = 0
    welcome_to_the_quiz()
    filtered_questions = filter_by_topic(questions)
    if not filtered_questions:
        print("No questions available for the selected topic. Exiting the quiz.")
        return score, qascore
    user_questions = how_many_questions()
    random.shuffle(filtered_questions)
    score, qascore = ask_questions(score, qascore, filtered_questions, user_questions)
    avg = average_score(score, qascore)
    play_again_or_end()  # Ask if the user wants to play again

def main_without_welcome_page():
    score = 0
    qascore = 0
    filtered_questions = filter_by_topic(questions)
    if not filtered_questions:
        print("No questions available for the selected topic. Exiting the quiz.")
        return score, qascore
    user_questions = how_many_questions()
    random.shuffle(filtered_questions)
    score, qascore = ask_questions(score, qascore, filtered_questions, user_questions)
    avg = average_score(score, qascore)
    play_again_or_end()  # Ask if the user wants to play again after this run

# Start the quiz
main()