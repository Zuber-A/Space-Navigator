'''
@author: Zuber Abdella
'''
# Imports
from tkinter import *
import random
import math
import time


class Spaceship:
    '''
    This class models Spaceship that will be rendered on the canvas
    '''

    def __init__(self, x=300, y=300, velX=23, velY=23, size=28, color='blue'):
        '''
        Constructor
        '''
        self._x = x
        self._y = y
        self._velX = velX
        self._velY = velY
        self._size = size
        self._color = color

    # This accessor gets the x coordinate of the spaceship
    def get_x(self):
        return self._x

        # This accessor gets the y coordinate of the spaceship

    def get_y(self):
        return self._y

    # This accessor gets the size of the spaceship
    def get_size(self):
        return self._size

        # Moves spaceship to the right

    def move_right(self, canvas):
        self._x += self._velX

    # Moves spaceship to the left
    def move_left(self, canvas):
        self._x -= self._velX

    # Moves spaceship up
    def move_up(self, canvas):
        self._y += self._velY

    # Moves spaceship down
    def move_down(self, canvas):
        self._y -= self._velY

    # Makes spaceship visible
    def render_ship(self, canvas):
        canvas.create_rectangle(self._x, self._y, self._x + self._size, self._y + self._size, fill=self._color)

class Asteroid:
    '''
    This class models the asteroids that will be rendered on the canvas
    '''

    def __init__(self, x=50, y=50, velX=10, velY=10, radius=20, color='grey'):
        '''
        Constructor
        '''
        self._x = x
        self._y = y
        self._velX = velX
        self._velY = velY
        self._radius = radius
        self._color = color

    # This accessor gets the x coordinate of the asteroid
    def get_x(self):
        return self._x

    # This accessor gets the y coordinate of the asteroid
    def get_y(self):
        return self._y

    # This accessor gets the radius of the asteroid
    def get_radius(self):
        return self._radius

    # This mutator allows user to set the x coordinate of the asteroid
    def set_x(self, newX):
        self.x = newX
        return newX

    # This mutator allows user to set the y coordinate of the asteroid
    def set_y(self, newY):
        self.y = newY
        return newY

    # This method moves the asteroid
    def move_asteroid(self, canvas):
        self._x += self._velX
        self._y += self._velY

    # This method makes the asteroid visible
    def render_asteroid(self, canvas):
        canvas.create_oval(self._x - self._radius,
                           self._y - self._radius,
                           self._x + self._radius,
                           self._y + self._radius,
                           fill=self._color)


class Game:
    def __init__(self, window):
        ''' Construct the GUI '''

        # Create the canvas
        self.window = window
        self.window.protocol('WM_DELETE_WINDOW', self.safe_exit)
        self.width = 600
        self.canvas = Canvas(self.window, bg='black',
                             width=self.width, height=self.width)
        self.canvas.pack()

        # Makes a list of asteroids
        self.asteroid_list = []

        # Create a spaceship from the imported class
        self.spaceship = Spaceship()

        self.terminated = False

        # Calls the function render
        self.render()

        # Bind commands with the arrow keys
        root.bind('<Right>', self.spaceship.move_right)
        root.bind('<Left>', self.spaceship.move_left)
        root.bind('<Down>', self.spaceship.move_up)
        root.bind('<Up>', self.spaceship.move_down)

        # Calls the function add_asteroid
        self.add_asteroid()


    # Creates asteroids and adds them to the canvas
    def add_asteroid(self):

        pos_vel = [13, 15]
        neg_vel = [-13, -15]
        rad = [16, 18, 20, 22]
        colors = ['skyblue', 'white', 'darkred', 'forestgreen', 'yellow', 'magenta']

        if not self.terminated:
            # create asteroids and add them to self.asteroid_list
            self.asteroid = [Asteroid(random.randint(20, 580), 20, 0, random.choice(pos_vel), random.choice(rad),
                                      random.choice(colors)),
                             Asteroid(random.randint(20, 580), 580, 0, random.choice(neg_vel), random.choice(rad),
                                      random.choice(colors)),
                             Asteroid(20, random.randint(20, 580), random.choice(pos_vel), 0, random.choice(rad),
                                      random.choice(colors)),
                             Asteroid(580, random.randint(20, 580), random.choice(neg_vel), 0, random.choice(rad),
                                      random.choice(colors))]
            for i in self.asteroid:
                self.asteroid_list.append(i)

            # Calls add_asteroid after a given time
            self.canvas.after(1500, self.add_asteroid)

    # This method makes the asteroids and the spaceship visible
    def render(self):

        if not self.terminated:
            self.canvas.delete(ALL)
            for asteroid in self.asteroid_list[:]:
                asteroid.move_asteroid(self.canvas)

                asteroid.render_asteroid(self.canvas)

                # Collision detector
                distance = math.sqrt(
                    (self.spaceship.get_x() - asteroid.get_x()) ** 2 + (self.spaceship.get_y() - asteroid.get_y()) ** 2)

                if distance < self.spaceship.get_size() * (2 / 5) + asteroid.get_radius():
                    print("Game Over! You lose!")
                    self.terminated = True

            # Renders the ship on the screen
            self.spaceship.render_ship(self.canvas)

            self.canvas.after(50, self.render)
            # nothing below this

    def safe_exit(self):
        ''' Turn off the event loop before closing the GUI '''
        self.terminated = True
        self.window.destroy()


if __name__ == '__main__':
    root = Tk()
    root.title('Game')
    app = Game(root)
    root.mainloop()
