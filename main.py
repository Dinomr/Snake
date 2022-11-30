#Importamos (turtle) y (Screen) Turtle para la serpiente y Screen para el tablero.
from turtle import Screen
from snake  import Snake 
from food import Food 
from scoreboard import Scoreboard 
import time

#Aquí modificamos el tabler como sus magnitudes, color, etc ...
screen = Screen() 
screen.setup(width=700, height=700) 
screen.bgcolor("black") 
screen.title("My Snake Game") 
screen.tracer(0)

snake = Snake()
food =  Food()
scoreboard = Scoreboard()

#Indicadores de la dirección de la serpiente.
screen.listen() 
screen.onkey(snake.up, "Up") 
screen.onkey(snake.down, "Down") 
screen.onkey(snake.left, "Left") 
screen.onkey(snake.right, "Right")

game_is_on = True 
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detectar la colision con los alimentos.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detectar la colision con las paredes.
    if snake.head.xcor() > 330 or snake.head.xcor() < -330 or snake.head.ycor() > 330 or snake.head.ycor() < -330: 
        game_is_on = False
        scoreboard.game_over()

    #Detectar la colision con sigo mismo.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10: 
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
