from tkinter import*
from PIL import ImageTk, Image
import os
import datetime as dt
#store score
score = []
# list of question 
questions = ['Print "Hello" in Java.',
             'Which GUI is used in this project?',
             'Which keyword is used in Python to use different modules?',
             'An ___________ is a computer program that directly executes instructions written in a programming language',
             'How do you destroy a tkinter window when root = Tk()?']
# list of answers
answers = ['System.out.println("Hello")',
           'tkinter',
           'import',
           'interpreter',
           'root.destroy()']
quests = len(questions)
window = Tk()
# set title
window.title('Welcome')
window2 = Tk()

window2.title('Setup')

name_label = Label(window2, text='What is your name?')
name_entry = Entry(window2, fg="Black", bg="Yellow", width=50)
next_but = Button(window2, padx=14,pady=14,bd=4,bg='orange',command=lambda:contin2(),text="Next >>>",font=("Courier New",16,'bold'))

window2.withdraw()

window3 = Tk()
window3.title('Ready?')
question = Label(window3, text='1 point for every correct answer and 0 for every incorrect one. Good Luck! Do your Best!!')
butt = Button(window3, padx=14,pady=14,bd=4,bg='orange',command=lambda:contin3(),text="Next >>>",font=("Courier New",16,'bold'))
window3.withdraw()
# stores current time
tim = str(dt.datetime.now())

def cont():
     window.destroy()
     window2.update()
     window2.deiconify()
     name_label.pack()
     name_entry.pack()
     next_but.pack()
     window2.mainloop()
 
def contin2():
     nameee = str(name_entry.get())
     window2.destroy()
     question = Label(window3, text=nameee+', Every correct question earns you a point. Every incorrect one gives none. Good Luck!')
     question.pack()
     butt.pack()
     window3.update()
     window3.deiconify()

def contin3():
     window3.withdraw()
     contin4()

def contin4():
     window4 = Tk()
     window4.title('Questions')
     question2 = Label(window4, text=questions[0])
     
     score_label = Label(window4, text= 'Score :' + str(len(score)))
     answer_entry = Entry(window4, fg="Black", bg="Yellow", width=50)
     butt2 = Button(window4, padx=14,pady=14,bd=4,bg='orange',command=lambda:window4.quit(),text="Next >>>",font=("Courier New",16,'bold'))
     question2.pack()
     score_label.pack()
     answer_entry.pack()
     butt2.pack()
     window4.mainloop()
     if (answer_entry.get() == answers[0]):
          print("Correct!")
          
          score.append(0)
     else:
          print("Incorrect! The correct answer is " + answers[0])
     answers.pop(0)
     questions.pop(0)
     window4.destroy()
     # if questions are left then continue quiz or create result file  
     if (0 < len(questions)):
          contin3()
     else:
          window3.destroy()
          # "w" - Write - Opens a file for writing, creates the file if it does not exist
          file = open(nameee+' report.txt', "w")
          namu = "Hello! This report has been autogenerated from the results of the quiz in PyQuiz.\nStart Time: "+str(tim)+" to "+str(dt.datetime.now())+ "\n Your score is "+str(len(score))+"/"+str(quests)+" \nThank you for answering PyQuiz's Quiz! We hope to see you again!"
          file.write(namu)
          file.close()

img = ImageTk.PhotoImage(Image.open("wel.jpg"))

panel = Label(window, image = img)
panel.pack(side = "top", fill = "both", expand = "yes")
button = Button(window,padx=14,pady=14,bd=4,bg='orange',command=lambda:cont(),text="Continue >>>",font=("Courier New",16,'bold')).pack()
window.mainloop()
