import turtle
import pygame

class Ball:
    '''Creating the ball object with turtle, adding the hit sound, checking collisions, movement and out of bounds'''
    def __init__(self, paddle_hit_sound):
        self.ball = turtle.Turtle() # Creates a new turtle object, the ball, let's shape it
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup() # Method to avoid drawing lines with the movement of the ball
        self.ball.goto(0, 0)
        self.ball.dx = 2  # Ball's speed in the x direction relative to the game world
        self.ball.dy = -2  # Ball's speed in the y direction relative to the game world
        self.paddle_hit_sound = paddle_hit_sound  # Store the paddle hit sound

    def move(self):
        '''Updates the ball's position based on its direction'''
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

    def check_collision_with_paddle(self, paddle):
        '''Checks if the ball hits a paddle and reverses its direction'''
        # Right paddle collision
        if (self.ball.xcor() > 340 and self.ball.xcor() < 350) and \
           (self.ball.ycor() < paddle.ycor() + 50 and self.ball.ycor() > paddle.ycor() - 50):
           self.ball.setx(340)
           self.ball.dx *= -1  # Reverse horizontal direction
           pygame.mixer.Sound.play(self.paddle_hit_sound)  # Play paddle hit sound

        # Left paddle collision
        elif (self.ball.xcor() < -340 and self.ball.xcor() > -350) and \
            (self.ball.ycor() < paddle.ycor() + 50 and self.ball.ycor() > paddle.ycor() - 50):
            self.ball.setx(-340)
            self.ball.dx *= -1  # Reverse horizontal direction
            pygame.mixer.Sound.play(self.paddle_hit_sound)  # Play paddle hit sound

    def check_collision_with_walls(self):
        '''Checks if the ball hits the top or bottom walls and makes it bounce back'''
        if self.ball.ycor() > 290:  # Top wall
            self.ball.sety(290)
            self.ball.dy *= -1  # Reverse vertical direction

        if self.ball.ycor() < -290:  # Bottom wall
            self.ball.sety(-290)
            self.ball.dy *= -1  # Reverse vertical direction

    def reset_position(self):
        '''Resets the ball to the center of the screen after a player scores'''
        self.ball.goto(0, 0)
        self.ball.dx *= -1  # Change direction after scoring

    def is_out_of_bounds(self):
        '''Checks if the ball has gone out of bounds (past the paddles)'''
        if self.ball.xcor() > 390 or self.ball.xcor() < -390:
            return True
        return False