# TODO
- Crear el cuerpo de la culebra.
- Mover la culebra.
- Controlar los movimientos de la culebra.
- Detectar  la colision con la comida.
- Manejar el puntaje.
- Detectar la colision con los muros.
- Detectar cuando colisione con sigo mismo.

## Crear el cuerpo de la serpiente

Lo primero que debemos de hacer es importar la libreria de turtle, con la cual vamos a hacer los graficos vecotriales que van a mostrar nuestro
juego en pantalla y luego creamos el cuerpo de la serpiente, esto lo hacemos creando un acrhivo en formato .py el cual entre otras cosas va a tener una posicion, color,
, forma y que tan grande va a hacer al principio la serpiente.

vamos a hacer uso de la programación orientada a objetos y se crea la clase Snake para que cuando se llame luego mediante la importación.

importarmos la libreria turtle y Damos la posicion inicial de la serpiente, cuanto se va a mover por cada refrescación en pantalla y hacia a donde tiene que ir por cada dirrección dada

    from turtle import Turtle
    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,0)]
    MOVE_DISTANCE = 20
    UP = 90
    DOWN = 270
    LEFT = 180 
    RIGHT = 0

Ahora ya dentro de la clase Snake lo que hacemos es crear la inicialización de la graficación creando una función __init__, vamos a decirle que tan grande
es el cuerpo de la serpiente declaradno una variable "segments" con una lista vacía y vamos a hacer uso de una función mas adelante llamada create_sanke
para crear cada parte del cuerpo de la serpiente y por ultimo vamos a indicarle que la cabeza de la serpiente tiene  indice cero de la lista segments

    class Snake:
        def __init__(self):
            self.segments = []
            self.create_snake()
            self.head = self.segments[0]

Ahora creamos la función que crea a la serpiente, la cual va a contener un ciclo con position como indice y que empiece desde con
cada elemento de la posiición incial
    
        def create_snake(self):
            for position in STARTING_POSITIONS:
                self.add_segment(position)

Ahora vamos a hacer que cada elemento que creamos se añada al cuerpo de la serpiente, vamos a especificar que forma va a conformar la serpiente,
que color tendrá. que deje de hacer una línea por los pixeles que va pasando el cursor y que siga añadiendo los elementos en la posición, por último solo
hacemos un append para que se añada al cuerpo de la serpiente

        def add_segment(self,position):
            new_segment = Turtle("circle")
            new_segment.color("green")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

Ahora creamos la función que va a extender o alargar nuestra serpiente

    def extend(self): 
        self.add_segment(self.segments[-1].position())

Ahora vamos a crear los respectivos cursores de la serpiente, esto va a indicarle a los nuevos elementos en que parte del cuerpo tienen que ser dibujados, y hacia donde tienen que seguir cuando se mueve la serpiente.

        def move(self):
            for seg_num in range(len(self.segments)- 1, 0, -1): 
                new_x = self.segments[seg_num -1].xcor()
                new_y = self.segments[seg_num -1].ycor()
                self.segments[seg_num].goto(new_x,new_y)
            self.head.forward(MOVE_DISTANCE)

Y ahora declaramos que cuando vaya en una dirrección no pueda ir a su opuesta, ya que sino colisionario consigo misma.

        def up(self):
            if self.head.heading() != DOWN:
                self.head.setheading(UP)

        def down(self):
            if self.head.heading() != UP:
                self.head.setheading(DOWN)

        def left(self):
            if self.head.heading() != RIGHT:
                self.head.setheading(LEFT)

        def right(self):
            if self.head.heading() != LEFT:
                self.head.setheading(RIGHT)

## Marcador
Ahora vamos a crear el puntaje de la serpiente por cada punto que se coma, esto lo hacemos indicandole donde se tiene que posicionar, tipo de letra que marca el nuevo puntaje por cada punto que haya sido comido