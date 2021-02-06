# Testing your knowledge by completing some Python questions

import turtle
import matplotlib.pyplot as plt

# Question 1 - Variables
# Create two variables x and y where ? is any number of your choice
#  And find the sum, division, subtraction and multiplication of those two variables
x = 2  # assigned an x variable equal to 2
y = 4  # assigned an y variable equal to 2

# Addition
print(x + y)

# Division
print(x / y)

# Subtraction
print(x - y)

# Multiplication
print(x * y)

# Question 2 - Lists
# Create a list of all the even numbers from 0 to 100
# Print the first 10 elements and find the length of this list
# And append a value of your choice to the end of this list

# (It can be any type!)
# x2 = 0
# while x2 <= 100:
#     print(x2*2)

my_list = list(range(0, 101, 2))  # Create the list
print(my_list)

print(my_list[0:10])  # Printing the first ten elements of the list

print(len(my_list))  # Finding the length of the list

my_list.append(True)  # Appending a value to this list - can be any type!
print(my_list)

# Question 3 - Assigning variables
# And using an if statement, find whether this integer is divisible by 5
# Get Python to print where it is or isn't

# x3 = 5
# if x3 == 5:
#     print(True)
# else:
#     print(False)

number = 835
if number % 5 == 0:
    print("number is  divisible by 5")
else:
    print("number is not divisible by 5")

# Question 4 - for loop
# Using a for loop, get Python to print the numbers 0 to 5

# x4 = 0
# for x4 == 5:
#     x4++:

for i in range(6):  # Remember we use 6 because the range command takes up to value n-1
    print(i)

# Question 5 - Turtle
# Draw a pentagon in Turtle
for i in range(5):  # A pentagon has five sides!
    turtle.right(72)  # This is the angle needed to produce a pentagon
    turtle.forward(100)  # This will give the length of the pentagon sides
turtle.done()  # turtle.done() keeps the turtle on screen after the drawing has completed


# Question 6 - Functions
# Create a function that tests whether three numbers (a, b, c) are a Pythagorean triple

def pythagorean_triple(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False


print(pythagorean_triple(3, 4, 5))  # This is True
print(pythagorean_triple(3, 9, 15))  # This is False
# Question 7 - Spot the Error!
# n = 5
# while n > 0:
#     n = n + 1
#     print(n)

# Question 8 - Plotting
# Create two lists (of size 5 or any size you want) and plot these lists against each other using matplotlib
list1 = [1, 6, 13, 16, 24]
list2 = [3, 7, 17, 28, 30]

plt.plot(list1, list2, c="blue", linewidth="1", label="A line!", linestyle="dashed",
         marker="s", markerfacecolor="purple", markersize=2)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Python Plot of a Line")
plt.legend()
plt.show()
