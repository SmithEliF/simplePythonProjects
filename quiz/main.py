from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# Adds the questions to a question bank

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while QuizBrain.still_has_questions(quiz):
    QuizBrain.next_question(quiz)

print(f"You've completed the quiz\nYour final score was {quiz.score}/{quiz.question_number}")
    