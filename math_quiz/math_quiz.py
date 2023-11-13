import random


def randomNumberGenerator(min, max):
    """
    This function returns a random integer between received 2 numbers
    :param min: int
    lower bound of range
    :param max: int
    upper bound of range
    :return: int
    a random integer between received 2 numbers
    """
    return random.randint(min, max)


def randomMathOperation():
    """
    This function randomly select of this mathematical operations
    :return: str
    a random math operation
    """
    return random.choice(['+', '-', '*'])


def calculatOperation(number1, number2, operation):
    """
    Calculates the input mathematical operation between 2 numbers
    for example: number1 = 3 , number2= 4, operation = '*'
    the result will be: number1 operation number2 = result
    or 3 * 4 = 12
    :param number1: int
    first input number
    :param number2: int
    second input number
    :param operation: str
    the mathematical operation to be calculated between them
    :return: int
    the outcome of above math operation
    """
    problem = f"{number1} {operation} {number2}"
    # Calculate mathematical operation respect to randomly selected(input) operation
    if operation == '+':
        answer = number1 + number2
    elif operation == '-':
        answer = number1 - number2
    else:
        answer = number1 * number2
    return problem, answer

def math_quiz():
    """
    This is the main part of code. It develop a for loop. at each loop a qestion in generated
    and asked from the user. If the user answer the question correctly the score adds up 1.
    at the end user can see its score from total possible achievable score.
    """
    score = 0
    TotalQuestionNumber = 3
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    # creat a for loop which repeats for the number of questions
    for _ in range(int(TotalQuestionNumber)):
        number1 = randomNumberGenerator(1, 10); number2 = randomNumberGenerator(1, 5); operation = randomMathOperation()
        # at each loop a qestion in generated and asked from the user.
        PROBLEM, ANSWER = calculatOperation(number1, number2, operation)
        print(f"\nQuestion: {PROBLEM}")
        # receive the user's answer
        # if the user enter a string instead of a number, it asks the user to enter a valid number again
        try:
            userAnswer = input("Your answer: ")
            userAnswer = int(userAnswer)
        except:
            print("Please enter a valid integer number")
            userAnswer = input("Your answer: ")
            userAnswer = int(userAnswer)

        if userAnswer == ANSWER:
        #   If the user answer the question correctly the score adds up 1
            print("Correct! You earned a point.")
            score = score + 1
        else:
        #   otherwise show user the correct answer
            print(f"Wrong answer. The correct answer is {ANSWER}.")
    # if the user answer more than 1/3 of questions, user will win, otherwise user will lose
    if score < TotalQuestionNumber//3:
        print(f"\nGame over! Your score is: {score}/{TotalQuestionNumber}")
    else:
        print(f"\nYou WIN! Your score is: {score}/{TotalQuestionNumber}")

if __name__ == "__main__":
    # if module is run as main module, math_quiz() will run
    math_quiz()
