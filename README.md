# Matrix Rain

![Matrix Rain](https://i.pinimg.com/564x/1c/7d/d0/1c7dd0f2d317ea003aedb902568ee967.jpg)

## Overview
Matrix Rain is a visual simulation inspired by the digital rain effect from the movie "The Matrix". It creates a mesmerizing display of falling characters, simulating the appearance of code cascading down the screen.

![Matrix Code](https://i.pinimg.com/736x/ed/74/2f/ed742f81f262beabda246a7bb6515b02.jpg)

## Features
- Dynamic and resizable window
- Real-time character rain effect
- Smooth animations with adjustable frame rates

## Requirements
- Python 3.x
- Pygame library

## Installation
1. Install Python 3.x from the [official website](https://www.python.org/).

2. Install Pygame library:
    ```bash
    pip install pygame
    ```

## Usage
1. Save the script as `matrix_rain.py`.

2. Run the script:
    ```bash
    python matrix_rain.py
    ```

## Code Explanation

### Imports and Initialization
The script begins by importing necessary libraries and initializing Pygame:
```python
import pygame
import random
import sys

pygame.init()
```
- `pygame`: Used for creating the graphical display.
- `random`: Used to randomly select characters for the rain effect.
- `sys`: Used to handle system-level operations like exiting the program.

### Constants and Screen Setup
The script defines the window dimensions, font size, and initializes the display window:
```python
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Matrix Rain - Ruby Poddar')

FONT_SIZE = 20
FONT = pygame.font.SysFont('consolas', FONT_SIZE)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0, 10)
```
- `WIDTH`, `HEIGHT`: Initial dimensions of the display window.
- `SCREEN`: Pygame display surface.
- `FONT_SIZE`: Size of the characters.
- `FONT`: Font used for rendering the characters.
- `GREEN`: Color of the characters.
- `BLACK`: Semi-transparent black for the fade effect.

### Characters and Drops Initialization
A list of characters and initial drop positions are set up:
```python
CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
columns = WIDTH // FONT_SIZE
drops = [0] * columns
clock = pygame.time.Clock()
```
- `CHARS`: String of characters used in the rain.
- `columns`: Number of columns of characters that fit in the window.
- `drops`: List tracking the position of the falling characters for each column.
- `clock`: Used to control the frame rate.

### Main Loop
The main loop handles events, updates the display, and manages the falling characters:
```python
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.size
            SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            columns = WIDTH // FONT_SIZE
            drops = [0] * columns
```
- Handles quit events and window resizing, adjusting the number of columns and drop positions accordingly.

### Drawing and Animation
Characters are randomly chosen and displayed, with drops reset when reaching the bottom of the screen:
```python
    fade_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    fade_surface.fill(BLACK)
    SCREEN.blit(fade_surface, (0, 0))

    for i in range(columns):
        text = random.choice(CHARS)
        x = i * FONT_SIZE
        y = drops[i] * FONT_SIZE

        char_surface = FONT.render(text, True, GREEN)
        SCREEN.blit(char_surface, (x, y))

        drops[i] += 1

        if drops[i] * FONT_SIZE > HEIGHT and random.random() > 0.95:
            drops[i] = 0

    pygame.display.flip()
    clock.tick(60)
```
- `fade_surface`: Creates a semi-transparent surface for the fade effect.
- `random.choice(CHARS)`: Selects a random character from the list.
- `SCREEN.blit()`: Renders the character onto the screen.
- `drops[i]`: Updates the position of the character.
- `pygame.display.flip()`: Updates the entire screen with the new frame.
- `clock.tick(60)`: Maintains a frame rate of 60 FPS.

## Conclusion
Enjoy the mesmerizing Matrix Rain effect on your screen! This project showcases how to use Pygame for creating dynamic and visually appealing graphical simulations.
