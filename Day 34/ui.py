from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=25, pady=25)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)

        # Canvas score
        self.score_ui = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("arial", 16, "normal"))
        self.score_ui.grid(column=1, row=0)

        # Canvas question
        self.question_text = self.canvas.create_text(150, 125, text="Question: ", font=("arial", 18, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons images
        false = PhotoImage(file="images/false.png")
        true = PhotoImage(file="images/true.png")

        # Button true or false
        self.true_button = Button(image=true, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(column=1, row=2)
        self.false_button = Button(image=false, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_ui.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="The quiz finished.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, right_answer):
        if right_answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)