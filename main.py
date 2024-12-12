import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Druel Quiz Game")
        self.root.geometry("600x500")
        self.root.configure(bg='navy')
        icon = tk.PhotoImage(file='./logo.PNG')
        self.root.iconphoto(True, icon)

        # Header frame for title and logo
        # self.header_frame = tk.Frame(root, bg='navy')
        # self.header_frame.pack(pady=10)

        # Add logo
        # self.logo = tk.PhotoImage(file='./logo.PNG') 
        # self.logo_label = tk.Label(self.header_frame, image=self.logo, bg='navy')
        # self.logo_label.pack(side=tk.LEFT, padx=10)

        # Title
        # self.title_label = tk.Label(self.header_frame, text="Quiz Game", font=("Arial", 24), bg='navy', fg='white')
        # self.title_label.pack(side=tk.LEFT)

        self.questions = {
            "Which one is not a state of matter?: " : "C",
            "At what temperature are Celsius and Fahrenheit equal?: " : "A",
            "How many bones are in the human body?: " : "D",
            "What is the only metal that is liquid at room temperature?: " : "A",
            "What is the chemical symbol for the element gold?: " : "B",
        }
        
        self.options = (
            ("A. Solid", "B. Gas", "C. Temperature", "D. Liquid"), 
            ("A. -40", "B. 35", "C. 40", "D. 0"),
            ("A. 500", "B. 10", "C. 75", "D. 206"),
            ("A. Mercury", "B. Bronze", "C. Lead", "D. Copper"),
            ("A. Be", "B. Au", "C. Li", "D. Al"),
        )

        self.guesses = []
        self.correct_guesses = 0
        self.question_num = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 16), bg='navy', fg='white')
        self.question_label.pack(pady=20)

        self.options_var = tk.StringVar(value="")

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.options_var, value=chr(65 + i), font=("Arial", 12), bg='navy', fg='white', selectcolor='navy')
            rb.pack(anchor='w')
            self.radio_buttons.append(rb)

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer, font=("Arial", 12, "bold"), bg='navy', fg='white', activebackground='white', activeforeground='navy', relief=tk.RAISED, bd=3, padx=10, pady=5)
        self.submit_button.pack(pady=20)

        self.result_label = tk.Label(root, text="", font=("Arial", 14), bg='navy', fg='white')
        self.result_label.pack(pady=20)

        # Next Button
        
        self.next_button = tk.Button(root, text="Next", command=self.next_question, font=("Arial", 12, "bold"), bg='navy', fg='white', activebackground='white', activeforeground='navy', relief=tk.RAISED, bd=3, padx=10, pady=5)
        self.next_button.pack(pady=20)
        
        

        self.display_question()

    def display_question(self):
        if self.question_num < len(self.questions):
            question = list(self.questions.keys())[self.question_num]
            self.question_label.config(text=question)
            for i, option in enumerate(self.options[self.question_num]):
                self.radio_buttons[i].config(text=option)
        else:
            self.display_score()

    def submit_answer(self):
        guess = self.options_var.get()
        self.guesses.append(guess)
        if guess == list(self.questions.values())[self.question_num]:
            self.correct_guesses += 1
        self.result_label.config(text="CORRECT" if guess == list(self.questions.values())[self.question_num] else "INCORRECT!")

    def next_question(self):
        self.question_num += 1
        self.options_var.set("")
        self.result_label.config(text="")
        if self.question_num < len(self.questions):
            self.display_question()
        else:
            self.display_score()

    def display_score(self):
        score = int(self.correct_guesses / len(self.questions) * 100)
        messagebox.showinfo("Results", f"Your score is {score}%\nThank you for playing!")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
