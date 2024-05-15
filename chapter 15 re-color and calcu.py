#chapter 15.1 auto calculate and re-color
import matplotlib.pyplot as plt

x_value = list(range(1, 1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value, y_value, s=40)

plt.title("Square number", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square value", fontsize = 14)
plt.tick_params(axis="both", which ='major', labelsize = 14)
plt.axis([0, 1100,0,1100000])
#color
#plt.scatter(x_value, y_value, c='red', edgecolors='None', s=40)
#colormap
plt.scatter(x_value, y_value, c=y_value,cmap=plt.cm.Blues,
            edgecolors='None', s=40)

plt.show()