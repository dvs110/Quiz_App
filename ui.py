THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:
    def __init__(self,quiz:QuizBrain): #we have to specify data type of quiz_brain object(quiz)[not mandatory]
        self.Quiz=quiz
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_label=Label(text="Score:0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.canvas=Canvas(width=300,height=250,bg="white")
        self.question_text=self.canvas.create_text(150,125,width=280,text="some ques text")
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        true_img = PhotoImage(file="C:/Users/Devang Sati/PycharmProjects/quizzler-app-start/images/true.png")
        false_img = PhotoImage(file="C:/Users/Devang Sati/PycharmProjects/quizzler-app-start/images/false.png")
        self.true_button=Button(image=true_img,highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(row=2,column=0)
        self.false_button = Button(image=false_img,highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.Quiz.still_has_questions():
            self.score_label.config(text=f"score:{self.Quiz.score}")
            self.Quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=self.Quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text="end of quiz")
            self.true_button.config(state="disabeled") #disable buttons
            self.false_button.config(state="disabeled")  # disable buttons
    def true_pressed(self):
        is_true=self.Quiz.check_answer("True")
        self.getfeedback(is_true)
    def false_pressed(self):
        is_true=self.Quiz.check_answer("False")
        self.getfeedback(is_true)
    def getfeedback(self,is_true):
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
