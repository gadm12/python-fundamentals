questions = [
    {
        "question": "Which data type is used to store multiple items in a single variable and is ordered and changeable?",
        "options": ["A. set", "B. tuple", "C. list"],
        "answer": "C",
    },
    {
        "question": "How do you create a variable with the numeric value 5 in Python?",
        "options": ["A. x = 5", "B. x == 5", "C. int x = 5"],
        "answer": "A",
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": ["A. .pyth", "B. .py", "C. .pt"],
        "answer": "B",
    },
    {
        "question": "Which operator is used for floor division (division that results in a whole number)?",
        "options": ["A. /", "B. %", "C. //"],
        "answer": "C",
    },
    {
        "question": "What is the output of print(type(10.5))?",
        "options": ["A. <class 'float'>", "B. <class 'int'>", "C. <class 'decimal'>"],
        "answer": "A",
    },
    {
        "question": "Which method can be used to remove any whitespace from both the beginning and the end of a string?",
        "options": ["A. len()", "B. strip()", "C. trim()"],
        "answer": "B",
    },
    {
        "question": "Which of these is NOT a valid variable name?",
        "options": ["A. my_var", "B. 2myvar", "C. _myvar"],
        "answer": "B",
    },
    {
        "question": "How do you start a 'for' loop in Python?",
        "options": ["A. for x in y:", "B. for x > y:", "C. for each x in y:"],
        "answer": "A",
    },
    {
        "question": "What is the correct way to create a dictionary in Python?",
        "options": [
            "A. {'name': 'John'}",
            "B. ['name': 'John']",
            "C. ('name': 'John')",
        ],
        "answer": "A",
    },
    {
        "question": "Which statement is used to stop a loop?",
        "options": ["A. stop", "B. exit", "C. break"],
        "answer": "C",
    },
]


def run_quiz(list_of_questions):
    score = 0
    print("welcome to the python Quiz!")
    print("Choose A, B, or C for each question. \n")

    for i, q in enumerate(list_of_questions, 1):
        print(f"Question {i}: {q["question"]}")

        for option in q["options"]:
            print(option)

        user_answer = input("Your answer: a").upper()

        if user_answer == q["answer"]:
            print("correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {q["answer"]}")
    print(f"You got {score} out of {len(list_of_questions)} correct")


run_quiz(questions)
