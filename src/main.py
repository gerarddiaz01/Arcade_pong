import turtle
from paddle import Paddle
from ball import Ball
from utils import draw_score
import time
import pygame
import os

def start_game():
    '''Function to start or resume the game'''
    global game_paused
    game_paused = False

def quit_game():
    '''Function to exit the game'''
    global game_running
    game_running = False

# Initialize pygame mixer
pygame.mixer.init()

# Initialize scores
score_a = 0
score_b = 0

# Draw the initial score
draw_score(score_a, score_b)

# Set up the screen
wn = turtle.Screen()
wn.title("Arcade Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # Turns off the screen updates

# Get the directory of the current script to have no issues loading the music files
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the sounds folder
sounds_dir = os.path.join(base_dir, "sounds")

# Construct absolute paths for the sound files
background_music_path = os.path.join(sounds_dir, "SalmonLikeTheFish - Glacier.mp3")
paddle_hit_sound_path = os.path.join(sounds_dir, "paddle_hit.mp3")
score_sound_path = os.path.join(sounds_dir, "chime_alert.mp3")

# Load background music and sound effects, make sure you are in the Sounds File
pygame.mixer.music.load(background_music_path) # Load background music
pygame.mixer.music.set_volume(0.5)  # Adjust volume (0.0 to 1.0)
pygame.mixer.music.play(-1)  # Play music in a loop

paddle_hit_sound = pygame.mixer.Sound(paddle_hit_sound_path)  # Load paddle hit sound
score_sound = pygame.mixer.Sound(score_sound_path)  # Load scoring sound

# Create paddles and ball
left_paddle = Paddle(-350)  # Pass numerical x_position for the left paddle
right_paddle = Paddle(350)  # Pass numerical x_position for the right paddle
ball = Ball(paddle_hit_sound)  # Pass the paddle hit sound to the Ball class

# Keyboard bindings
wn.listen()
wn.onkeypress(left_paddle.move_up, "w")
wn.onkeypress(left_paddle.move_down, "s")
wn.onkeypress(right_paddle.move_up, "Up")
wn.onkeypress(right_paddle.move_down, "Down")

# Add a flag to control the game loop
game_running = True

# Add a flag to control whether the game is paused
game_paused = True

# Bind the Spacebar key to start or resume the game
wn.onkeypress(start_game, "space")

# Bind the Escape key to quit the game
wn.onkeypress(quit_game, "Escape")

# Main game loop
while game_running: # Use the game_running flag to control the loop
    wn.update() # Refreshes the screen
    
    if not game_paused:  # Only move the ball if the game is not paused
        # Move the ball
        ball.move()
    
    # Check for collisions
    ball.check_collision_with_walls()  # Check for wall collisions
    ball.check_collision_with_paddle(left_paddle.paddle)
    ball.check_collision_with_paddle(right_paddle.paddle)
    
    # Check for scoring
    if ball.is_out_of_bounds():
        if ball.ball.xcor() > 390:  # Ball went past the right paddle
            score_a += 1
        elif ball.ball.xcor() < -390:  # Ball went past the left paddle
            score_b += 1
    
        # Play scoring sound
        pygame.mixer.Sound.play(score_sound)

        # Reset the ball position
        ball.reset_position()

        # Pause the game after scoring
        game_paused = True
    
        # Update the score on the screen
        draw_score(score_a, score_b)
    
    time.sleep(0.01)  # Add a small delay to slow down the game, control frame rate and ensure smooth animations

# Exit the program gracefully
wn.bye()  # Close the turtle graphics window