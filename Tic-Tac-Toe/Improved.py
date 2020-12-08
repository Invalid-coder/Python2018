from math import sqrt
from Main import *

class Window:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.setup(630, 630)
        self.window.title('Противостояние X vs 0')
        turtle.hideturtle()
        turtle.speed(15)
        turtle.pensize(4)
        self.play = True
        self.pieces = []
        self.nextTurn = 'X'
        self.draw_field()
        self.window.onclick(self.clicked)
        self.window.mainloop()

    def draw_field(self):
        x = -315
        y = 315
        for i in range(9):
            self.pieces.append(Field(x,y))
            for j in range(9):
                x = x + 70
                if j in (2, 5):
                    x = x - 210
                    y = y - 70
                elif j == 8:
                    y = y + 140
            if i in (2, 5):
                x = -315
                y = y - 210

        turtle.pencolor('grey')
        turtle.up()
        turtle.goto(-315, 245)
        turtle.down()
        turtle.forward(630)
        turtle.up()
        turtle.goto(-315, 175)
        turtle.down()
        turtle.forward(630)

        turtle.up()
        turtle.goto(-315, 35)
        turtle.down()
        turtle.forward(630)
        turtle.up()
        turtle.goto(-315, -35)
        turtle.down()
        turtle.forward(630)

        turtle.up()
        turtle.goto(-315, -175)
        turtle.down()
        turtle.forward(630)
        turtle.up()
        turtle.goto(-315, -245)
        turtle.down()
        turtle.forward(630)

        # vertical bars
        turtle.up()
        turtle.goto(-245, 315)
        turtle.setheading(-90)
        turtle.down()
        turtle.forward(630)
        turtle.up()
        turtle.goto(-175, 315)
        turtle.setheading(-90)
        turtle.down()
        turtle.forward(630)

        turtle.up()
        turtle.goto(-35, 315)
        turtle.setheading(-90)
        turtle.down()
        turtle.forward(630)
        turtle.up()
        turtle.goto(35, 315)
        turtle.setheading(-90)
        turtle.down()
        turtle.forward(630)
        turtle.up()

        turtle.up()
        turtle.goto(175, 315)
        turtle.down()
        turtle.forward(630)
        turtle.up()
        turtle.goto(245, 315)
        turtle.down()
        turtle.forward(630)

        turtle.setheading(0)
        turtle.pencolor('black')

        turtle.up()
        turtle.goto(-315, 105)
        turtle.down()
        turtle.forward(630)

        turtle.up()
        turtle.goto(-315, -105)
        turtle.down()
        turtle.forward(630)

        turtle.up()
        turtle.goto(-105, 315)
        turtle.setheading(-90)
        turtle.down()
        turtle.forward(630)

        turtle.up()
        turtle.goto(105, 315)
        turtle.down()
        turtle.forward(630)

    def drawPieces(self,square,subsquare):
        x = -315
        y = 315
        for i, piece in enumerate(self.pieces):
            for j,k in enumerate(piece.pieces):
                if  k == 'X' and i == square and j == subsquare and not(self.pieces[square].value):
                    self.pieces[square].cross(x,y)
                elif k == '0' and i == square and j == subsquare and not(self.pieces[square].value):
                    self.pieces[square].nought(x,y)
                x = x + 70
                if j in (2, 5):
                    x = x - 210
                    y = y - 70
                elif j == 8:
                    y = y + 140
            if i in (2, 5):
                x = -315
                y = y - 210

        turtle.pensize(10)
        if self.pieces[0].value != ' ' and self.pieces[0].value and self.pieces[0].value == self.pieces[1].value == self.pieces[2].value:
            turtle.up()
            turtle.color('red' if self.pieces[0].value == 'X' else 'blue')
            turtle.goto(-315, 210)
            turtle.setheading(0)
            turtle.down()
            turtle.forward(630)
            self.play = False
            self.window.title('Победитель - {}'.format(self.pieces[0].value))
        elif self.pieces[0].value != ' ' and self.pieces[0].value and self.pieces[0].value == self.pieces[3].value == self.pieces[6].value:
            turtle.up()
            turtle.color('red' if self.pieces[0].value == 'X' else 'blue')
            turtle.goto(-210, 315)
            turtle.setheading(-90)
            turtle.down()
            turtle.forward(630)
            self.play = False
            self.window.title('Победитель - {}'.format(self.pieces[0].value))
        elif self.pieces[4].value != ' ' and self.pieces[4].value and self.pieces[3].value == self.pieces[4].value == self.pieces[5].value:
            turtle.up()
            turtle.color('red' if self.pieces[4].value == 'X' else 'blue')
            turtle.goto(-315, 0)
            turtle.setheading(0)
            turtle.down()
            turtle.forward(630)
            self.play = False
            self.window.title('Победитель - {}'.format(self.pieces[0].value))
        elif self.pieces[4].value != ' ' and self.pieces[4].value and self.pieces[1].value == self.pieces[4].value == self.pieces[7].value:
            turtle.up()
            turtle.color('red' if self.pieces[4].value == 'X' else 'blue')
            turtle.goto(0, 315)
            turtle.setheading(-90)
            turtle.down()
            turtle.forward(630)
            self.play = False
            self.window.title('Победитель - {}'.format(self.pieces[4].value))
        elif self.pieces[4].value != ' ' and self.pieces[4].value and self.pieces[0].value == self.pieces[4].value == self.pieces[8].value:
            turtle.up()
            turtle.color('red' if self.pieces[4].value == 'X' else 'blue')
            turtle.goto(-295, 295)
            turtle.setheading(-45)
            turtle.down()
            turtle.forward((630 * sqrt(2)) - 60)
            self.play = False
            self.window.title('Победитель - {}'.format(self.pieces[4].value))
        elif self.pieces[4].value != ' ' and self.pieces[4].value and self.pieces[2].value == self.pieces[4].value == self.pieces[6].value:
            turtle.up()
            turtle.color('red' if self.pieces[4].value == 'X' else 'blue')
            turtle.goto(295, 295)
            turtle.setheading(-135)
            turtle.down()
            turtle.forward((630 * sqrt(2)) - 60)
            self.play = False
            self.window.title('Победитель - {}'.format(self.pieces[4].value))
        elif self.pieces[8].value != ' ' and self.pieces[8].value and self.pieces[8].value == self.pieces[7].value == self.pieces[6].value:
            turtle.up()
            turtle.color('red' if self.pieces[8].value == 'X' else 'blue')
            turtle.goto(-315, -210)
            turtle.setheading(0)
            turtle.down()
            turtle.forward(630)
            self.play = False
            self.window.title('Победитель - {}'.format(self.pieces[8].value))
        elif self.pieces[8].value != ' ' and self.pieces[8].value and self.pieces[8].value == self.pieces[5].value == self.pieces[2].value:
            turtle.up()
            turtle.color('red' if self.pieces[8].value == 'X' else 'blue')
            turtle.goto(210, 315)
            turtle.setheading(-90)
            turtle.down()
            turtle.forward(630)
            self.play = False
            self.window.title('Победитель - {}'.format(self.pieces[8].value))
        elif all(piece.value for piece in self.pieces):
             self.play = False
             self.window.title('Ничья')
             turtle.pensize(7)

             turtle.pencolor('black')
             turtle.up()
             turtle.goto(-295, 295)
             turtle.setheading(-45)
             turtle.down()
             turtle.forward((630 * sqrt(2)) - 60)

             turtle.up()
             turtle.goto(295, 295)
             turtle.setheading(-135)
             turtle.down()
             turtle.forward((630 * sqrt(2)) - 60)

        turtle.pensize(4)

    def clicked(self,x,y):
        if self.play:
            column = (x + 315) // 210
            row = (-y + 315) // 210
            square = int(column + row * 3)
            if not (self.pieces[square].value):
                subsquare,next = self.pieces[square].clicked(x,y,self.nextTurn)
                if next:
                    if self.nextTurn == 'X':
                        self.nextTurn = '0'
                    else:
                        self.nextTurn = 'X'
                    self.drawPieces(square,subsquare)
        else:
            self.window.clear()
            self.window.title('Противостояние X vs 0')
            turtle.hideturtle()
            turtle.speed(15)
            turtle.pensize(4)
            self.play = True
            self.nextTurn = 'X'
            self.pieces = []
            self.draw_field()
            self.window.onclick(self.clicked)
            self.window.mainloop()

window = Window()

