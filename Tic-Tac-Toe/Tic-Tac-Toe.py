import turtle
from math import sqrt

class Window:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.setup(600, 600)
        self.window.title('Противостояние X vs 0')
        turtle.hideturtle()
        turtle.delay(3)
        turtle.pensize(4)
        self.play = True
        self.pieces = ['', '', '', '', '', '', '', '', '']
        self.nextTurn = 'X'
        self.draw_field()
        self.window.onclick(self.clicked)
        self.window.mainloop()

    def draw_field(self):
        turtle.up()
        turtle.goto(-300, 100)
        turtle.down()
        turtle.forward(600)
        turtle.up()
        turtle.goto(-300, -100)
        turtle.down()
        turtle.forward(600)
        # vertical bars
        turtle.up()
        turtle.goto(-100, 300)
        turtle.setheading(-90)
        turtle.down()
        turtle.forward(600)
        turtle.up()
        turtle.goto(100, 300)
        turtle.down()
        turtle.forward(600)
    def cross(self,x,y):
        turtle.up()
        turtle.goto(x + 20, y - 20)
        turtle.setheading(-45)
        turtle.down()
        turtle.pencolor('blue')
        turtle.forward(226)
        turtle.up()
        turtle.goto(x + 180, y - 20)
        turtle.setheading(-135)
        turtle.down()
        turtle.forward(226)
        turtle.up()
        turtle.pencolor('red')

    def nought(self,x,y):
        turtle.up()
        turtle.goto(x + 100,y - 180)
        turtle.setheading(0)
        turtle.down()
        turtle.circle(80)
        turtle.up()
        turtle.pencolor('blue')

    def drawPieces(self,square):
        x = -300
        y = 300
        for i, piece in enumerate(self.pieces):
            # print(x,y)
            if piece == 'X' and i == square:
                self.cross(x,y)
            elif piece == '0' and i == square:
                self.nought(x,y)
            x = x + 200
            if x > 100:
                x = -300
                y = y - 200
        turtle.pensize(7)
        if self.pieces[0] and self.pieces[0] == self.pieces[1] == self.pieces[2]:
            turtle.up()
            turtle.goto(-300, 200)
            turtle.setheading(0)
            turtle.down()
            turtle.forward(600)
            self.play = False
            self.window.title('Победитель - {}'.format(self.pieces[0]))
        elif self.pieces[0] and self.pieces[0] == self.pieces[3] == self.pieces[6]:
            turtle.up()
            turtle.goto(-200, 300)
            turtle.setheading(-90)
            turtle.down()
            turtle.forward(600)
            self.play = False
            self.window.title('Победитель - {}'.format(self.pieces[0]))
        elif self.pieces[4] and self.pieces[3] == self.pieces[4] == self.pieces[5]:
            turtle.up()
            turtle.goto(-300, 0)
            turtle.setheading(0)
            turtle.down()
            turtle.forward(600)
            self.play = False
            self.window.title('Победитель - {}'.format(self.pieces[4]))
        elif self.pieces[4] and self.pieces[1] == self.pieces[4] == self.pieces[7]:
            turtle.up()
            turtle.goto(0, 300)
            turtle.setheading(-90)
            turtle.down()
            turtle.forward(600)
            self.play = False
            self.window.title('Победитель - {}'.format(self.pieces[4]))
        elif self.pieces[4] and self.pieces[0] == self.pieces[4] == self.pieces[8]:
            turtle.up()
            turtle.goto(-280, 280)
            turtle.setheading(-45)
            turtle.down()
            turtle.forward((600 * sqrt(2)) - 60)
            self.play = False
            self.window.title('Победитель - {}'.format(self.pieces[4]))
        elif self.pieces[4] and self.pieces[2] == self.pieces[4] == self.pieces[6]:
            turtle.up()
            turtle.goto(280, 280)
            turtle.setheading(-135)
            turtle.down()
            turtle.forward((600 * sqrt(2)) - 60)
            self.play = False
            self.window.title('Победитель - {}'.format(self.pieces[4]))
        elif self.pieces[8] and self.pieces[8] == self.pieces[7] == self.pieces[6]:
            turtle.up()
            turtle.goto(-300, -200)
            turtle.setheading(0)
            turtle.down()
            turtle.forward(600)
            self.play = False
            self.window.title('Победитель - {}'.format(self.pieces[8]))
        elif self.pieces[8] and self.pieces[8] == self.pieces[5] == self.pieces[2]:
            turtle.up()
            turtle.goto(200, 300)
            turtle.setheading(-90)
            turtle.down()
            turtle.forward(600)
            self.play = False
            self.window.title('Победитель - {}'.format(self.pieces[8]))
        elif all(self.pieces):
            self.play = False
            self.window.title('Ничья')
            turtle.pensize(7)

            turtle.pencolor('blue')
            turtle.up()
            turtle.goto(-300, 200)
            turtle.setheading(0)
            turtle.down()
            turtle.forward(600)

            turtle.pencolor('red')
            turtle.up()
            turtle.goto(-300, 0)
            turtle.setheading(0)
            turtle.down()
            turtle.forward(600)

            turtle.pencolor('blue')
            turtle.up()
            turtle.goto(-300, -200)
            turtle.setheading(0)
            turtle.down()
            turtle.forward(600)

            turtle.pencolor('red')
            turtle.up()
            turtle.goto(-200, 300)
            turtle.setheading(-90)
            turtle.down()
            turtle.forward(600)

            turtle.pencolor('blue')
            turtle.up()
            turtle.goto(0, 300)
            turtle.setheading(-90)
            turtle.down()
            turtle.forward(600)

            turtle.pencolor('red')
            turtle.up()
            turtle.goto(200, 300)
            turtle.setheading(-90)
            turtle.down()
            turtle.forward(600)

            turtle.pencolor('black')
            turtle.up()
            turtle.goto(-280, 280)
            turtle.setheading(-45)
            turtle.down()
            turtle.forward((600 * sqrt(2)) - 60)

            turtle.up()
            turtle.goto(280, 280)
            turtle.setheading(-135)
            turtle.down()
            turtle.forward((600 * sqrt(2)) - 60)

        turtle.pensize(4)

    def clicked(self,x,y):
        if self.play:
            column = (x + 300) // 200
            row = (-y + 300) // 200
            square = int(column + row * 3)
            # print(x,'x')
            # print(y,'y')
            # print(column,'column')
            # print(row, 'row')
            # print(square, 'square')
            if not (self.pieces[square]):
                self.pieces[square] = self.nextTurn
                if self.nextTurn == 'X':
                    self.nextTurn = '0'
                else:
                    self.nextTurn = 'X'
                self.drawPieces(square)
        else:
            self.window.clear()
            self.window.title('Противостояние X vs 0')
            turtle.hideturtle()
            turtle.delay(3)
            turtle.pensize(4)
            self.play = True
            self.pieces = ['', '', '', '', '', '', '', '', '']
            self.nextTurn = 'X'
            self.draw_field()
            self.window.onclick(self.clicked)

window = Window()
