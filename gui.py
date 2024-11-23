from tkinter import *

quizapp = Tk() #instantiate an instance of a window

quizapp.geometry("550x550")

quizapp.title("Druel Quiz App")

#CONVERT THE PHOTO FROM PNG TO PHOTO IMAGE

icon = PhotoImage(file='./logo.PNG')
quizapp.iconphoto(True, icon)
quizapp.config(background="#F4C2C2")

quizapp.mainloop() #Place windows on computer screen, listens for events