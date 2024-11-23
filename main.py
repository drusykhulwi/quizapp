def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("***********************")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ").upper()
        guesses.append(guess) 

        correct_guesses += check_answer(questions.get(key), guess)  
        question_num += 1   
        
    display_score(correct_guesses, guesses)        


def check_answer(answer, guess):
    
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("INCORRECT!")
        return 0
    

def display_score(correct_guesses, guesses):
    print("------------------")
    print("RESULTS")
    print("------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()    

    print("Guesses: ", end="") 
    for i in guesses:
        print(i, end=" ")
    print()    

    score = int(correct_guesses / len(questions)* 100) 
    print(f"Your score is {score}%")

def play_again():
    response = input("Do you want to play again? (yes or no): ").upper()
    
    if response == "YES":
        return True
    else:
        return False
    

questions = {
    "Which one is not a state of matter?: " : "C",
    "At what temperature are celcius and farenheit equal?: " : "A",
    "How many bones are in the human body: " : "D",
    "What is the only metal that is liquid at room temperature?: " : "A",
    "What is the chemical symbol for the element gold?: ": "B",
}

# make a 2D tuple of answers we have four options
options = (
    (
        "A. Solid",
        "B. Gas", 
        "C. Temperature",
        "D.Liquid"
    ), 
    (
        "A.-40", 
        "B.35", 
        "C.40",
        "D.0"
    ),
    (
        "A.500", 
        "B.10", 
        "C.75",
        "D.206"
    ),
    (
        "A.Mercury", 
        "B.Bronze", 
        "C.Lead",
        "D.Copper"
    ),
    (
        "A.Be", 
        "B.Au", 
        "C. Li",
        "D.Al"
    ),
)     

new_game()

while play_again():
    new_game()

print("Thank you for playing! Bye")    