from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random
from art import logo

print(logo)


# lista de questões (objetos)
question_bank = []

for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

# reordena os elementos na lista de modo aleatório a cada vez que o programa é executado
random.shuffle(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Você completou o Quiz.")
print(f"Sua pontuação final foi: {quiz.score}/{quiz.question_number}.")
print("Parabéns!")
