class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        total_question = len(self.question_list)
        if self.question_number < total_question:
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {current_question.text} (True/False):? ")
        self.check_ans(user_ans, current_question.answer)

    def check_ans(self, user_ans, correct_ans):
        if correct_ans.lower() == user_ans.lower():
            print("Your answer is correct")
            self.score += 1
        else:
            print(f"You've enter wrong ans.")
        print(f"Correct ans is {correct_ans}")
        print(f"Your current score is {self.score}/{self.question_number}")