import random


python_questions = {
    "What is the keyword to define a function in Python?": "def",
    "How do you print 'Hello' in Python?": "print('Hello')",
    "What symbol is used for comments in Python?": "#",
    "Which function do you use to get user input in Python? (No Syntax)": "input",
    "What is the result of 2 + 2 in Python?": "4",
    "How do you declare an empty variable called 'var' in Python?": "var=''",
    "____ is an immutable  data structure in Python that can act as a list?": "tuple",
    "How do you access the first element of a list called 'numbers'?": "numbers=[0]",
    "What keyword is used to run loops until a certain condition is met in Python?": "while",
    "How do you check the length of a list called 'nums;?": "len(nums)",
    "What is the keyword to define a class in Python?": "class",
    "We normally handle exceptions in Python using try ______ blocks?": "except",
    "What is the boolean value for True in Python? (capitalized) ": "True",
    "Which keyword do you use to check if a value exists in a list?": "in",
    "You can us __-strings to concatenate two strings in Python": "f",
    "What is the output of bool(0)?": "False",
    "Dictionaries store key - _______ pairs": "value",
    "What is the name of the method to delete an item from a list temporarily (No syntax)?": "pop",
    "What is the output of type(10)?": "<class 'int'>",
    "The last element in a list is 'len(list)'": "Using 'if', e.g., if x > 5: print('Big number!')"
}

def python_trivia_game():
    questions_list = list(python_questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list, total_questions)

    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Your answer: ").lower().strip()
        
        correct_answer = python_questions[question]

        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is {correct_answer}.\n")

    print(f"Your score is {score}/5 questions")

python_trivia_game()