#chapter 15 random walk

from random import choice    

class RandomWalk():
    def __init__(self, num_points = 500):
        self.num_points = num_points

        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        while len(self.x_value) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_distance * x_direction

            y_direction = choice([1, -1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_distance * y_direction

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)


