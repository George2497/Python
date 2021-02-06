# Importing the relevant modules
import matplotlib.pyplot as plt

# Plotting Graphs in Python

# Very basic plot - we want something better!
# x = [1, 3, 5, 10]  # This is what we are plotting
# plt.plot(x)
# plt.show()  # This will show the plot we are plotting

# Plotting x and y against each other
# y = [7, 12, 21, 22]
# plt.plot(x, y)
# plt.show()

# Let's plot a lovely looking plot

# Line 1 - Points
x = [3, 9, 14]
y = [2, 7, 30]
# Plotting x and y
plt.plot(x, y, c="red", linewidth=2, label="Line 1")

# Line 2 - Points
x2 = [1, 15, 18]
y2 = [0, 3, 12]
# Plotting x2 and y2
plt.plot(x2, y2, c="green", linewidth=2, label="Line 2", linestyle="dashed",
         marker='s', markerfacecolor="orange", markersize=10)

# Label the axes and give the plot a title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Two lines!")

# Limits of the axis
plt.ylim(1, 10)
plt.xlim(0, 30)

# Show the legend on the plot
plt.legend()

# Get Python to show the plot
plt.show()

