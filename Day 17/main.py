from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

for question in question_data:

    question_bank.append(Question(question["question"], question["correct_answer"]))

new_question = QuizBrain(question_bank)

while new_question.still_has_question():
    new_question.next_question()

print("You've completed the quiz!!!")
print(f"Your final score was : {new_question.score}/{len(question_bank)}")