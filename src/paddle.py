import turtle

class Paddle:
    '''Creating the paddle object with turtle, shaping the paddles and creating movement up and down'''
    def __init__(self, x_position):
        self.paddle = turtle.Turtle() # Create a new turtle object, the paddles, let's shape them
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=6, stretch_len=1) # Stretch the turtle object to make it rectangular
        self.paddle.penup() # Method to avoid drawing lines with the movement of the paddles
        self.paddle.goto(x_position, 0)

    def move_up(self):
        y = self.paddle.ycor()
        if y < 250:  # Assuming the screen height is 500
            self.paddle.sety(y + 20)

    def move_down(self):
        y = self.paddle.ycor()
        if y > -240:  # Assuming the screen height is 500
            self.paddle.sety(y - 20)