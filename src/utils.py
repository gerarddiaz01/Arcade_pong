import turtle
# Creates a turtle object specifically for displaying the score
score_turtle = turtle.Turtle()
score_turtle.hideturtle() # Hide the turtle cursor
score_turtle.speed(0) # Set the turtle's animation speed to the fastest
score_turtle.color("white") # Set the text color to white
score_turtle.penup() # Lift the pen to avoid drawing lines

def draw_score(score_a, score_b):
    """Draws the current score on the screen."""
    score_turtle.clear()  # Clear only the score area
    score_turtle.goto(0, 260)
    score_turtle.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

def reset_game():
    """Resets the game state for a new round."""
    # This function can be expanded to reset scores, positions, etc.
    pass

# Constants for screen dimensions and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = "black"
PADDLE_COLOR = "white"
BALL_COLOR = "white"