from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 200  # Lower the number higher the speed
SPACE_SIZE = 50  # Size of the food and body parts of the snake.
BODY_PARTS = 3  # Body parts of a snake when game begin.
SNAKE_COLOR = '#00FF00'  # Green
FOOD_COLOR = '#FF0000'   # Red
BACKGROUND_COLOR = '#000000'   # Black

class Snake:
    def __init__(self):
        self.body = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tag='snake')
            self.squares.append(square)
class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE

        y = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]
        # Food object
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag='food')

def next_turn(snake, food):
    x, y = snake.coordinates[0]   # Head of the Snake
    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR)
    snake.squares.insert(0, square)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global  score
        score += 1
        label.config(text='score : {}'.format(score))
        canvas.delete('food')
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y<0 or y >= GAME_HEIGHT:
        return True

    for BODY_PARTS in snake.coordinates[1:]:
        if x == BODY_PARTS[0] and y == BODY_PARTS[1]:
            return True
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70), text='GAME OVER', fill = 'Red', tag='game_over')


window = Tk()
window.title('Snake Game')
window.resizable(False, False)

score = 0
direction = 'down'
label = Label(window, text='Score : {}'.format(score), font=('Consolas', 40))
label.pack()

# Canvas is a widget used to display the graphics in the application.
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

# To Center the Game Board.

window_width = window.winfo_width()   # Width in Pixels of a Window
window_height = window.winfo_height()  # Height in pixels of a window
screen_width = window.winfo_screenwidth()  # Width in pixels of a Screen
screen_height = window.winfo_screenheight()  # Width in pixels of a Screen

x = int(screen_width/2) - int(window_width/2)
y = int(screen_height/2) - int(window_height/2)

window.geometry(f'{window_width}x{window_height}+{x}+{y}')

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))


snake = Snake()
food = Food()
next_turn(snake, food)


window.mainloop()