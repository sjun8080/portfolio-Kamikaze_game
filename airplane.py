
import turtle

class PlayerAirplane:
    def __init__(self):
        """Initialize the player's airplane."""
        self.airplane = turtle.Turtle()
        self.airplane.penup()
        self.airplane_speed = 8

        try:
            self.airplane.shape("images/airplane.gif")
        except:
            self.airplane.shape("square")
            self.airplane.color("red")

        self.airplane.goto(-300, 0)  # Start position

    def move_up(self):
        """Move the airplane up, with screen boundary check."""
        y = self.airplane.ycor()
        if y < 250:
            self.airplane.sety(y + self.airplane_speed)

    def move_down(self):
        """Move the airplane down, with screen boundary check."""
        y = self.airplane.ycor()
        if y > -250:
            self.airplane.sety(y - self.airplane_speed)

    def move_right(self):
        """Move the airplane right, with screen boundary check."""
        x = self.airplane.xcor()
        if x < 300:
            self.airplane.setx(x + self.airplane_speed)

    def collision_attack(self, ship):


        if self.airplane.distance(ship) < 20:
                print("Nobody is a winner at war")
                return True
        return False
