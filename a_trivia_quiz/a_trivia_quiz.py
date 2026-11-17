questions = {
    "Which keyword is used to define a function in Python? " : "def",
    "What is the name od the build-in function that returns the number of items in an object? " : "len",
    "What keyword is user to handle exceptions inside a try block? " : "except",
    "Which data type represents an order, unchangeable (immutable) collection of elements? " : "tuple",
    "What keyword is used to exit a loop prematurely? " : "break",
    "What keyword is used to import a module into script? " : "import",
    "What is the name od the special value used to represent the absence of a value or a null value? " : "none",
    "Which keyword is used to return a values from a generator function without terminating it? " : "yield",
    "What special method (dunder method) acts as the constructor and initializes a new object? " : "__init__",
    "Which logical operator returns True only if both of its operands are True? " : "and"
}

def ask_question(question, answer):
    user = input(f"{question}").strip().lower()
    return user == answer

score = 0

for question, answer in questions.items():
    if ask_question(question, answer):
        print("Correct!")
        score += 1
    else:
        print(f"No, the answer was {answer}.")

print(f"\nYour final score: {score}/{len(questions)}")