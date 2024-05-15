#Chapter 15 mpl squares
import matplotlib.pyplot as plt

squares = [1,4,9,16,25,36,49]
input_values = [1,2,3,4,5,6,7]

plt.plot( input_values, squares, linewidth =5)
#Set up title value, x-label and y-label
plt.title("Square number", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square's value", fontsize = 14)
plt.tick_params(axis="both", labelsize = 14)
#plot 1 to 7 square number as line
plt.show()

#scatter
x_value = [1,2,3,4,5,6,7]
y_value = [1,4,9,16,25,36,49]

plt.scatter(x_value, y_value, s=100)
#Set up title value, x-label and y-label
plt.title("Square number", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square value", fontsize = 14)
plt.tick_params(axis="both", which ='major', labelsize = 14)
plt.show()

