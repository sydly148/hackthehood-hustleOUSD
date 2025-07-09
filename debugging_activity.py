# Debugging Activity - Sydney Ly
























# Code Snippet 1
x = 10
y = 2
result = x / y # Zero Division error, fixed by changing y to a value that's not 0
print('Result: ', result)

#Code Snippet 2
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i]) # off by one error, delete the + 1

#Code Snippet 3
def calculate_area(radius): # missing colon
    area = 3.14 * radius ** 2
    return area

radius = 5
print(calculate_area(radius))

#Code Snippet 4
def is_even(number):
    if number % 2 == 0: # missing colons
        return True
    else:
        return False

#Code Snippet 5
for i in range(5): # missing colons
    print(i)

#Code Snippet 6
def greet(name):
    return "Hello, " + name #missing + operator to add strings

print(greet("Alice"))

#Code Snippet 7
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number # indentation error, should be indented
print("Sum of numbers: ", sum)



#Code Snippet 8
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) #never ending recursion loop, should be - 1 

print(factorial(5))

#Code Snippet 9
name = input("Enter your name: ")
if name == "Alice" or name == "Bob": # need another conditional statement
    print("Hello, " + name)
else:
    print("Hello, stranger!")

#Code Snippet 10
def divide_numbers(x, y):
    if y == 0:
        return "Can't divide by zero!" 
    else:
        result = x / y 
        return result

num1 = 10
num2 = 2 # Zero division error 
print(divide_numbers(num1, num2))