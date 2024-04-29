import time

# get start time
st = time.time()

x = 623240.775936
ans = 789.456

def approximation_method(x):
    """
    function that gets squareroot using approximation method

    input: int
    return: the square root of input
    """
    start = 0
    end = x
    guess = 0
    epsilon = 0.001
    step = 0.001

    number_guesses = 0

    while abs(guess**2 - x) > epsilon and guess ** 2 > x:
        if guess**2 == x:
            break
        if guess ** 2 > x:
            break
        guess += step
        number_guesses += 1

    return f'answer: {guess} || number of guesses: {number_guesses}'

def bisection(x):
    """
    function that gets the squareroot using the bisection method

    input: int
    return: returns the square root of the input
    """
    start = 0
    end = x
    epsilon = 0.001
    number_guesses = 0
    guess = x

    while abs(guess**2 - x) > epsilon:
        print(f'guess: {guess} difference: {abs(guess**2 - x)} ')
        if guess ** 2 > x:
            end = guess
        else:
            start = guess

        guess = (start + end)/2
        number_guesses += 1

    return f'answer: {guess} || number of guesses: {number_guesses}'

def newton_method(x):
    """
    function that get the squareroot using the newton method
    """
    guess = x
    epsilon = 0.001
    number_guesses = 0

    while abs(guess**2 - x) > epsilon:
        print(f'guess: {guess} difference: {abs(guess**2 - x)}')
        guess = 0.5*(guess + (x/guess))
        number_guesses += 1

    return f'answer: {guess} || number of guesses: {number_guesses}'

#print(approximation_method(x))
#print(bisection(x))
print(newton_method(x))

# get end time
et = time.time()

elapsed_time = et - st
print(f'execution time: {elapsed_time * 10**3}')
