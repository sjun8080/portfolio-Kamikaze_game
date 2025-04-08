import time
import turtle
import os
from airplane import PlayerAirplane
from ship import battleShip
from flak import flakShells

# setup the screen size
screen = turtle.Screen()
screen.title("Pacific Theater - Kamikaze Run")
screen.setup(width=800, height=600)
screen.tracer(0)

# set airplane and battleship shape
try:
    screen.register_shape("images/airplane.gif")
    screen.register_shape("images/battleship.gif")
    print("All images registered successfully")
except Exception as e:
    print(f"Error registering images: {e}")

# Set Background
try:
    screen.bgpic("images/ocean.gif")
except:
    print("Background image not found, using blue background.")
    screen.bgcolor("blue")
game_is_on = True

# instance of airplane
player = PlayerAirplane()
battleship = battleShip()
flak = flakShells()

instructions = turtle.Turtle()
instructions.hideturtle()
instructions.penup()
instructions.goto(0, -140)
instructions.color("white")
instructions.write("Kamikaze Run: Use arrow keys to fly カミカゼラン 矢印キーを使って飛ぶ",align="center", font=("Arial", 14, "normal"))

# Key setup
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_right, "Right")

# Main game loop
while game_is_on:
    time.sleep(0.1)

    battleship.move()  # Without this, the battleship won't move
    flak.update_shells()  # Handles both creation & movement
    flak.move_shells()

    screen.update()

    if player.collision_attack(battleship.ship):
        instructions.clear()
        time.sleep(0.5)  # Short delay before clearing screen to ensure message is visible
        instructions.write("Nobody is a winner at war 戦争に勝者はいない ", align="center",
                           font=("Arial", 15, "bold"))
        screen.update()  # Update to display the game over message
        time.sleep(3)  # Keep the message visible for 3 seconds
        game_is_on = False  # End the game
        screen.update()
        time.sleep(1)
        screen.bye()

    if flak.check_collision(player.airplane):  # If airplane is hit by flak
        instructions.clear()
        time.sleep(0.5)  # Short delay before clearing screen to ensure message is visible
        instructions.write("Attack failed! 攻撃は失敗した！ ", align="center", font=("Arial", 15, "bold"))
        screen.update()  # Update to display the game over message
        time.sleep(3)  # Keep the message visible for 3 seconds
        game_is_on = False  # End the game

        # Wait for the last update to be visible before closing the window
        screen.update()  # Final update before closing
        time.sleep(1)  # Optional: wait a bit longer before closing the window
        screen.bye()  # Close the Turtle graphics window

