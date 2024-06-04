from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.canvas=Canvas(height=200,width=300)
        self.question_text=self.canvas.create_text(150,125,
                                                   text="soooommmmmeeeee",
                                                   width=280,
                                                   font=("Arial",16,"italic"))

        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.label=Label(text=f"Score",fg="white",bg=THEME_COLOR)
        self.label.grid(row=0,column=1)
        true_image=PhotoImage(file="images/true.png")
        self.rbutton=Button(image=true_image,highlightthickness=0,command=self.true_p)
        self.rbutton.grid(row=2,column=0)
        wrong_image=PhotoImage(file="images/false.png")
        self.lbutton = Button(image=wrong_image,highlightthickness=0,command=self.false_p)
        self.lbutton.grid(row=2, column=1)
        self.get_next_question()


        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.label.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text="you've reached the end of the quiz")
            self.lbutton.config(state="disabled")
            self.rbutton.config(state="disabled")

    def true_p(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false_p(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
