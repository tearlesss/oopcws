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
# stores length of questions ie no of questions
quests = len(questions)
#creates an empty window 
window = Tk()
# set title
window.title('Welcome')
# creates 2nd window
window2 = Tk()
# set title 
window2.title('Setup')
# creates label to ask for name 
name_label = Label(window2, text='What is your name?')
# stores name , Entry func to enter the name
name_entry = Entry(window2, fg="Black", bg="Yellow", width=50)
# creates button
next_but = Button(window2, padx=14,pady=14,bd=4,bg='orange',command=lambda:contin2(),text="Next >>>",font=("Courier New",16,'bold'))
# withdraw() -> Removes the window from the screen, without destroying it.
window2.withdraw()

window3 = Tk()
window3.title('Ready?')
question = Label(window3, text='1 point for every correct answer and 0 for every incorrect one. Good Luck! Do your Best!!')
butt = Button(window3, padx=14,pady=14,bd=4,bg='orange',command=lambda:contin3(),text="Next >>>",font=("Courier New",16,'bold'))
window3.withdraw()
# stores current time
tim = str(dt.datetime.now())

# def-> keyword for creating functions

def cont():
     # destroy window ie closes it
     window.destroy()
     # update is used to update data but here actually to call the window
     window2.update()
     # deiconify->Displays the window, after using either the iconify or the withdraw methods.
     window2.deiconify()
     # pack means placing evrything to the window
     name_label.pack()
     name_entry.pack()
     next_but.pack()
     window2.mainloop()
 
def contin2():
     # gets the name and turns it into the string
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

     # remove question and ans from original array
     answers.pop(0)
     questions.pop(0)
     window4.destroy()
     # if questions r left then continue quiz or create result file  
     if (0 < len(questions)):
          contin3()
     else:
          window3.destroy()
          # opens a file or actually create it
          # "w" - Write - Opens a file for writing, creates the file if it does not exist
          file = open(str(dt.datetime.now())+' report.txt', "w")
          namu = "Hello! This report has been autogenerated from the results of the quiz in PyQuiz "+str(tim)+ " Your score is "+str(len(score))+"/"+str(quests)+" Thank you for answering PyQuiz's Quiz! We hope to see you again!"
          file.write(namu)
          file.close()
# PhotoImage class is used to add image to widgets, icons etc 
# initialize tinkter compatible image 
img = ImageTk.PhotoImage(Image.open("wel.jpg"))
# creates a label with an image
panel = Label(window, image = img)
# This geometry manager organizes widgets in blocks before placing them in the parent widget
     #expand − When set to true, widget expands to fill any space not otherwise used in widget's parent.
     #fill − Determines whether widget fills any extra space allocated to it by the packer, or keeps its own minimal dimensions: NONE (default), X (fill only horizontally), Y (fill only vertically), or BOTH (fill both horizontally and vertically).
     # side − Determines which side of the parent widget packs against: TOP (default), BOTTOM, LEFT, or RIGHT.
panel.pack(side = "top", fill = "both", expand = "yes")
# creates button       padding-x        border backgroud  lambda is used to pass the next function
# lambda actually returns functions
# pack() method:It organizes the widgets in blocks before placing in the parent widget.
button = Button(window,padx=14,pady=14,bd=4,bg='orange',command=lambda:cont(),text="Continue >>>",font=("Courier New",16,'bold')).pack()
#There is a method known by the name mainloop() is used when your application is ready to run. mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.
window.mainloop()
# extra understanding
# iconify() Turns the window into an icon (without destroying it). To redraw the window, use deiconify. Under Windows, the window will show up in the taskbar. When the window has been iconified, the state method returns “iconic”.
#withdraw() Removes the window from the screen (without destroying it). To redraw the window, use deiconify. When the window has been withdrawn, the state method returns “withdrawn”. 