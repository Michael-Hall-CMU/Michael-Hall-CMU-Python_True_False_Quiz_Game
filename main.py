from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from random import shuffle

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

shuffle(question_bank)
quiz = QuizBrain(question_bank)

max_questions = int(input("How many Questions would you like to do? "))

while max_questions > quiz.question_number and quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")