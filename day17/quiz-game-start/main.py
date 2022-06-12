from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []


for i in question_data:
    question = i['text']
    ans = i['answer']
    bank = Question(question, ans)
    question_bank.append(bank)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the Quiz")
print(f"Your Final score was: {quiz.score}")