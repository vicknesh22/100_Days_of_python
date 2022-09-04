THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # setting up the window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        #self.window.minsize(width=500, height=900)
        # setting canvas
        self.canvas = Canvas(width=400, height=350, bg="white", highlightthickness=0)
        self.quiz_text = self.canvas.create_text(150, 130, width=380, text="Amazon acquired twitch", fill="black",
                                                 font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50, padx=30)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 20, "bold"))
        self.score_label.grid(column=1, row=0)

        # image button
        self.right_image = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0, command=self.true_ans)
        self.right_button.grid(column=0, row=2)

        self.wrong_image = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0, command=self.wrong_ans)
        self.wrong_button.grid(column=1, row=2)

        # initializing the window with entry question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You have reached end of the Quizz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")


    def true_ans(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def wrong_ans(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
