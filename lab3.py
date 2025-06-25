# Lab 3

# Task 1: Working with Strings
food = 'buldak carbonara'
#print(food[:3]) #Print first 3 characters
#print(food[-3:]) #Print last 3 characters
first_last = food[0] + food[-1] #combine first and last character
#print(first_last)
food_list = food.split()
#print(food_list)
joined_food = ' '.join(food_list)
#print(joined_food)

# Task 2: Working with Lists
number_list = [1, 7675647456, 32, -5, 0, 234]
number_list.append(67)
#print(number_list)
number_list.insert(3, 1000)
#print(number_list)
number_list.pop()
#print(number_list)
number_list.remove(number_list[1])
#print(number_list)
#print(number_list[:3])
#print(number_list[-3:])


# Task 3: Working with Dictionaries
books = {'Suzanne Collins': 'The Hunger Games', 
         'George Orwell': '1984', 
         'Rick Riordan': 'Percy Jackson', 
         'Jeff Kinney': 'Diary of a Wimpy Kid'}
#print(books.keys())
#print(books.values())
#print(books.get('Rick Riordan'))
books.pop('Rick Riordan')
#print(books)
del books['Suzanne Collins']
print(books)