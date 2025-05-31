# Arcade Pong Game

Arcade Pong is a simple implementation of the classic Pong game using Python's `turtle` graphics module. The project aimed to provide a fun and interactive way to learn about game development, object-oriented programming, and integrating multiple Python files for better organization. Additionally, we incorporated sound effects using `pygame` to enhance the user experience.

---

## Learning Context

This was built as part of my 3rd month learning Python (April 2025), and was my first structured experience using turtle and pygame in a modular, object-oriented way. 

---

## Project Structure

```
arcade_pong
├── src
│   ├── main.py        # Entry point of the game
│   ├── paddle.py      # Paddle class for player controls
│   ├── ball.py        # Ball class for game mechanics
│   ├── utils.py       # Utility functions and constants
│   ├── sounds/        # Folder containing sound files
│       ├── SalmonLikeTheFish - Glacier.mp3
│       ├── paddle_hit.mp3
│       ├── chime_alert.mp3
├── requirements.txt    # List of dependencies
└── README.md           # Project documentation
```

---

## How to Run the Game

1. Ensure you have Python installed on your machine. This project uses Python's built-in turtle module, so no additional installations are required.
2. Clone the repository or download the project files to your local machine.
3. Navigate to the `arcade_pong/src` directory in your terminal or command prompt.
4. Run the game by executing the following command:

   ```
   python main.py
   ```

---

## Controls

- Player 1 (Left Paddle):
  - Move Up: `W`
  - Move Down: `S`

- Player 2 (Right Paddle):
  - Move Up: `Up Arrow`
  - Move Down: `Down Arrow`

- Play/Resume game : `Space`

- Exit game: `Escape`

---

## Future Enhancements

- Introduce difficulty levels by adjusting the ball speed.
- Allow for single-player mode against an AI opponent.

Feel free to contribute to the project by adding new features or improving existing ones!

---

## Project Recap:

### Tools and Libraries Used

1. **Turtle**:
   - Used to create the graphical elements of the game, such as the paddles, ball, and score display.
   - Methods like `penup()`, `goto()`, `xcor()`, and `ycor()` were used to control the movement and positioning of game objects.

2. **Pygame**:
   - Used to add background music and sound effects for paddle hits and scoring events.
   - Functions like `pygame.mixer.Sound.play()` and `pygame.mixer.music.play()` were used to handle audio playback.

3. **Time**:
   - Used `time.sleep()` to control the frame rate of the game and ensure smooth animations.

4. **OS Module**:
   - Used `os.path` to dynamically construct absolute paths for sound files, ensuring they are loaded correctly regardless of the current working directory.

5. **Modular Programming**:
   - The project was divided into multiple files (`main.py`, `paddle.py`, `ball.py`, `utils.py`) to improve readability and maintainability.

---

### Key Features of the Game

1. **Dynamic Paddle and Ball Movement**:
   - The paddles can move up and down using keyboard controls.
   - The ball moves dynamically, bouncing off walls and paddles, and resets when a player scores.

2. **Score Display**:
   - The score is displayed at the top of the screen and updates dynamically when a player scores.

3. **Sound Effects**:
   - Background music plays in a loop during the game.
   - Paddle hits and scoring events trigger distinct sound effects.

4. **Interactive Controls**:
   - Players can start or resume the game with the `Space` key and exit the game with the `Escape` key.

---

## Challenges Encountered and Solutions

### Challenge 1: Collision Detection
   - **Challenge**: Ensuring the ball bounces correctly off paddles and walls.
   - **Solution**: Implemented methods like `check_collision_with_paddle` and `check_collision_with_walls` in the `Ball` class to handle collisions dynamically.

### Challenge 2: Ball Speed and Direction
   - **Challenge**: Controlling the ball's speed and ensuring it moves in the correct direction after collisions.
   - **Solution**: Used `dx` and `dy` variables to control the ball's speed and direction, and reversed their values upon collisions.

### Challenge 3: Sound Integration
   - **Challenge**: Adding sound effects for paddle hits and scoring events.
   - **Solution**: Used `pygame.mixer.Sound` to load and play sound effects, passing the sound objects to the `Ball` class for paddle hit sounds.

### Challenge 4: Sound File Paths
   - **Challenge**: Ensuring the sound files are loaded correctly regardless of the current working directory.
   - **Solution**: Used the `os` module to dynamically construct absolute paths for the sound files:
     ```python
     base_dir = os.path.dirname(os.path.abspath(__file__))
     sounds_dir = os.path.join(base_dir, "sounds")
     background_music_path = os.path.join(sounds_dir, "SalmonLikeTheFish - Glacier.mp3")
     ```
     This approach ensures the sound files are always loaded from the `sounds` folder inside the `src` directory.

### Challenge 5: Game Pausing and Resuming
   - **Challenge**: Pausing the game after a player scores and resuming it with a key press.
   - **Solution**: Introduced a `game_paused` flag in `main.py` to control the game state and bound the `Space` key to resume the game.

### Challenge 6: Code Organization
   - **Challenge**: Keeping the code readable and maintainable as the project grew.
   - **Solution**: Divided the code into multiple files:
     - `main.py`: Handles the game loop and user input.
     - `paddle.py`: Defines the `Paddle` class.
     - `ball.py`: Defines the `Ball` class and its behavior.
     - `utils.py`: Contains utility functions like `draw_score`.

---

### What I Learned

1. **Using Libraries Effectively**:
   - Gained hands-on experience with `turtle` and `pygame`, learning how to integrate graphics and sound into a Python project.

2. **Object-Oriented Programming**:
   - Learned how to design and use classes (`Paddle`, `Ball`) to encapsulate game logic and behavior.

3. **Error Handling and Debugging**:
   - Encountered and resolved issues like undefined variables, incorrect collision logic, and sound playback errors.

4. **Code Organization**:
   - Improved code readability and maintainability by dividing the project into multiple files and using modular programming.

5. **AI Assistance**:
   - Used AI tools to understand the `turtle` and `pygame` libraries, debug issues, and learn best practices for game development.

---

## Potential Next Steps

- Add AI opponent for single-player mode
- Implement scoring logic based on time survived
- Add player name input and scoreboard file

---

### Conclusion

This project was a valuable learning experience, combining graphics, sound, and game logic into a cohesive program. By overcoming challenges and implementing features step by step, I created a fun and interactive game that demonstrates the power of Python for game development. The modular structure and clear documentation make this project easy to understand and extend.