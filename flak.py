from turtle import Turtle
import random

COLORS = ["red", "orange"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class flakShells:
    """Initialize flak shells for shooting towards the airplane."""
    def __init__(self):
        self.all_shells = []
        self.shell_speed = STARTING_MOVE_DISTANCE

    def create_shell(self):
        random_chance = random.randint(1,6) #slow down the cars
        if random_chance == 1:
            new_shell = Turtle("square")
            new_shell.shapesize(stretch_wid=0.1, stretch_len=2)
            new_shell.penup()
            new_shell.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_shell.goto(300, random_y)
            self.all_shells.append(new_shell)
    def move_shells(self):
        """Move all shells to the left towards the airplane."""
        for shell in self.all_shells:
            shell.backward(self.shell_speed)
    def check_collision(self,airplane):
        """Check if any shell collides with the airplane."""
        for shell in self.all_shells:
            if shell.distance(airplane) < 20:
                print("Hit!")
                return True
        return False
    def update_shells(self):
        """Combine creation and movement into one call."""
        self.create_shell()
        self.move_shells()

    '''def level_up(self):
        """Increase the shell speed for difficulty scaling."""
        self.shell_speed += MOVE_INCREMENT'''
