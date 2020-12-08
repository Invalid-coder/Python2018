import turtle
from math import sqrt

class Field:
    def __init__(self,x,y):
        self.value = ''
        self.pieces = ['', '', '', '', '', '', '', '', '']
        self.x = x
        self.y = y

    def cross(self, x, y):
        turtle.up()
        turtle.goto(x + 7, y - 7)
        turtle.setheading(-45)
        turtle.down()
        turtle.pencolor('blue')
        turtle.forward(78)
        turtle.up()
        turtle.goto(x + 63, y - 7)
        turtle.setheading(-135)
        turtle.down()
        turtle.forward(78)
        turtle.up()
        turtle.pencolor('red')

    def nought(self, x, y):
        turtle.up()
        turtle.goto(x + 35, y - 62)
        turtle.setheading(0)
        turtle.down()
        turtle.pencolor('red')
        turtle.circle(84 // 3)
        turtle.up()
        turtle.pencolor('blue')

    def checkField(self,x,y,square):
        if self.pieces[0] and self.pieces[0] == self.pieces[1] == self.pieces[2]:
            self.value = self.pieces[0]
            color = 'blue' if self.pieces[0] == 'X' else 'red'
            self.rectangle(self.x,self.y,color)
        elif self.pieces[0] and self.pieces[0] == self.pieces[3] == self.pieces[6]:
            self.value = self.pieces[0]
            color = 'blue' if self.pieces[0] == 'X' else 'red'
            self.rectangle(self.x, self.y, color)
        elif self.pieces[4] and self.pieces[3] == self.pieces[4] == self.pieces[5]:
            self.value = self.pieces[4]
            color = 'blue' if self.pieces[4] == 'X' else 'red'
            self.rectangle(self.x, self.y, color)
        elif self.pieces[4] and self.pieces[1] == self.pieces[4] == self.pieces[7]:
            self.value = self.pieces[4]
            color = 'blue' if self.pieces[4] == 'X' else 'red'
            self.rectangle(self.x, self.y, color)
        elif self.pieces[4] and self.pieces[0] == self.pieces[4] == self.pieces[8]:
            self.value = self.pieces[4]
            color = 'blue' if self.pieces[4] == 'X' else 'red'
            self.rectangle(self.x, self.y, color)
        elif self.pieces[4] and self.pieces[2] == self.pieces[4] == self.pieces[6]:
            self.value = self.pieces[4]
            color = 'blue' if self.pieces[4] == 'X' else 'red'
            self.rectangle(self.x, self.y, color)
        elif self.pieces[8] and self.pieces[8] == self.pieces[7] == self.pieces[6]:
            self.value = self.pieces[8]
            color = 'blue' if self.pieces[8] == 'X' else 'red'
            self.rectangle(self.x, self.y, color)
        elif self.pieces[8] and self.pieces[8] == self.pieces[5] == self.pieces[2]:
            self.value = self.pieces[8]
            color = 'blue' if self.pieces[8] == 'X' else 'red'
            self.rectangle(self.x, self.y, color)
        elif all(self.pieces):
            self.value = ' '
            self.rectangle(self.x, self.y, 'white')

    def clicked(self,x,y,nextTurn):
        if not(self.value):
            column = ((x + 315) // 70) % 3
            row = ((-y + 315) // 70) % 3
            square = int(column + row * 3)
            if not (self.pieces[square]):
                self.pieces[square] = nextTurn
                self.checkField(x,y,square)
                return square,True
            else:
                return square,False

    def rectangle(self,x,y,color):
        turtle.color(color)
        turtle.setposition(x+2,y-2)
        turtle.setheading(0)
        turtle.right(0)
        turtle.begin_fill()
        turtle.forward(206)
        turtle.right(90)
        turtle.forward(206)
        turtle.right(90)
        turtle.forward(206)
        turtle.right(90)
        turtle.forward(206)
        turtle.end_fill()

