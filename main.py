questions = (
    "Which one is not a state of matter?: ",
    "At what temperature are celcius and farenheit equal?: ",
    "How many bones are in the human body: ",
    "What is the only metal that is liquid at room temperature?: ",
    "What is the chemical symbol for the element gold?: ",
)

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

answers = ("C", "A", "D", "A", "B")

guesses = []

score = 0

question_num = 0

for question in questions:
    print("********************")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")    
    question_num += 1    

score = score / len(questions) * 100

if score >= 70 :
    print(f"Your score is {score}%, Excellent!")
elif score >= 50 :
    print(f"Your score is {score}%,Good Try!")    
else:
    print(f"Your score is {score}%,You'll get it next time!")    
