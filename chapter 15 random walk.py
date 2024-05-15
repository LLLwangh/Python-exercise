#chapter 15 random walk
import  matplotlib.pyplot as plt
from random_walk import RandomWalk

def make_walk():
    rw = RandomWalk(50000)
    rw.fill_walk()
    # Generating a list of colors based on the order of the walk
    colors = range(len(rw.x_value))
    plt.scatter(rw.x_value, rw.y_value, c=colors, cmap='viridis', edgecolors='none', s=1)
    plt.show()


make_walk()

while True:
    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        print("Exiting the program.")
        break
    elif keep_running.lower() == 'y':
        make_walk()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")