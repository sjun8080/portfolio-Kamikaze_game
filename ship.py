import turtle

class battleShip:
    def __init__(self):
        """Initialize the battleship."""
        self.ship = turtle.Turtle()
        self.ship.penup()
        self.ship_speed = 2

        try:
            self.ship.shape("images/battleship.gif")
        except:
            self.ship.shape("square")
            self.ship.color("gray")

        self.ship.goto(300, 0)
        self.ship_direction = 1

    def move(self):
        new_y = self.ship.ycor() + (self.ship_speed * self.ship_direction)
        if new_y > 250 or new_y < -250:
            self.ship_direction *= -1
        self.ship.sety(new_y)

