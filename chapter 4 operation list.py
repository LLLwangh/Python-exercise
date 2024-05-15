#Operation to the list
pizza = ["Pepperoni","Hawaiian","Supreme"]
for flavor in pizza:
    print("I like" + " " + flavor + " " + "pizza\n")
print("I really love pizza!")

pets = ["dog","cat","bird"]
for pet in pets:
    print("A"+ " " + pet.title() + " " + "would be a great pet\n")
print("Any of these animals would make a great pet.")

for value in range(1,21):
    print(value)

# Generate numbers from 1 to 1,000,000 using list comprehension
numbers = [i for i in range(1, 1000001)]

# Compute the sum of the numbers using the sum() function
total_sum = sum(numbers)

print("The sum of numbers from 1 to 1,000,000 is:", total_sum)

#4-6
odd_number = list(range(1,21,2))
print(odd_number)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

#4-10
