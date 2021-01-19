# Day 17 - Final challenge "Quiz game".


from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

    # answer_reply = input(f"{quest['text']}?. true or false: ")
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"You're final score was: {quiz.score}/{quiz.question_number}.")
