# Debugging Activity - Sydney Ly

# Code Snippet 1
x = 10
y = 2
result = x / y # ZeroDivisionError
print('Result: ', result)

# Code Snippet 2
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i]) # Off by one error

# Code Snippet 3
def calculate_area(radius): # SyntaxError: missing colon
    area = 3.14 * radius ** 2
    return area

radius = 5
print(calculate_area(radius))

# Code Snippet 4
def is_even(number):
    if number % 2 == 0: # SyntaxError: missing colons
        return True
    else:
        return False

# Code Snippet 5
for i in range(5): # SyntaxError: missing colon
    print(i)

# Code Snippet 6
def greet(name):
    return "Hello, " + name # missing + sign

print(greet("Alice"))

# Code Snippet 7
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number # IndentationError
print("Sum of numbers: ", sum)

# Code Snippet 8
def factorial(n): # Correct, no errors
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

# Code Snippet 9
name = input("Enter your name: ")
if name == "Alice" or name == "Bob": #always evaluates to True
    print("Hello, " + name)
else:
    print("Hello, stranger!")

# Code Snippet 10
def divide_numbers(x, y):
    if y == 0:
        return "Can't divide by zero!"
    else:
        result = x / y 
        return result

num1 = 10
num2 = 0 # Division by Zero Error
print(divide_numbers(num1, num2))