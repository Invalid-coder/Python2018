from tkinter import *
from Ship import *
import random

class Field(Canvas):
    def __init__(self,app, parent,name, *args,
                 rows=10,cols=10,p=True,ai=False,bordercolor='blue',
                 ratio=0.85,highlightbackground = 'blue',grid='blue', **kwargs):

        Canvas.__init__(self,parent,*args,**kwargs)
        self['highlightbackground'] = highlightbackground
        self.name = name
        self.parent = parent
        self.app = app
        self.ai = ai
        self.ready = False
        self.rows = rows
        self.cols = cols
        self.bordercolor = bordercolor
        self.ratio = 1
        self.cellwidth = int(self['width']) // self.cols
        self.cellheight = int(self['height']) // self.rows
        self.ships = {1:4,2:3,3:2,4:1}
        self.current_ships = {1: 0, 2: 0, 3: 0, 4: 0}
        self.ships_obj = {}
        self.current_ship = 1
        self.grid = []
        self.grid_ = []

        for row in range(self.rows):

            self.grid.append([])
            self.grid_.append([])

            for col in range(self.cols):

                self.grid[row].append(None)
                self.grid_[row].append(None)

        self.draw_grid(outline=grid)
        self.bind('<Button-1>', self.on_click)

        if p:
            
            self.selected_ship = Ship(1,4,self,121,121,151,151,4,4,0,'yellow')
            self.selection = False
            self.draw = True
            self.dx = 30
            self.dy = 30
            self.c = 0
            self.bind('<Motion>',self.motion)
            self.bind('<Button-3>',self.rotate)

        else:

            self.selected_ship = None
            self.selection = False
            self.draw = True


    def tag(self, row, col):
        '''Побудувати рядок з тегом для клітинки (row, col).

           Наприклад: 't001002'
        '''
        return 't{:0>3}{:0>3}'.format(row, col)

    def draw_grid(self,outline='blue'):

        for row in range(self.rows):
            for col in range(self.cols):

                xstart = col * self.cellwidth + 1
                ystart = row * self.cellheight + 1
                xend = xstart + self.cellwidth + 2
                yend = ystart + self.cellheight + 2
                self.grid_[row][col] = (xstart, ystart, xend, yend)

                # зобразити прямокутник та встановити його тег
                self.create_rectangle(xstart, ystart, xend, yend,
                                      width=self['bd'], fill=self['bg'],
                                      outline=outline,
                                      tags=self.tag(row, col))


    def create_ship(self,row, col,type,number):

        if not self.selection:

            self.dx = self.dy = 30
            self.c = 0
            self.ships_obj['{}_{}'.format(self.selected_ship.type,self.selected_ship.number)] = self.selected_ship

        left = col * self.cellwidth  # лівий верхній кут зображення (х)
        top = row * self.cellheight  # лівий верхній кут зображення (y)
        r2 = (1 - self.ratio) / 2
        xstart = left + int(self.cellwidth * r2) + 1
        ystart = top + int(self.cellheight * r2) + 1
        xend = left + int(self.cellwidth * (1 - r2)) + 1
        yend = top + int(self.cellheight * (1 - r2)) + 1

        self.itemconfigure('{}_{}'.format(self.selected_ship.type, self.selected_ship.number), outline='black')

        for row,col in self.selected_ship.cells:

            self.grid[row][col] = '{}_{}'.format(self.selected_ship.type,self.selected_ship.number)

        if self.ships[self.current_ship]:

            self.draw = False

            self.selected_ship = Ship(self.current_ship, self.ships[self.current_ship], self, xstart, ystart, xend, yend, row, col,0,'yellow')

        else:

            self.selected_ship = None
            self.selection = False

    def move_ship(self,row, col):

        left = col * self.cellwidth  # лівий верхній кут зображення (х)
        top = row * self.cellheight  # лівий верхній кут зображення (y)
        r2 = (1 - self.ratio) / 2
        xstart = left + int(self.cellwidth * r2) + 1
        ystart = top + int(self.cellheight * r2) + 1
        xend = left + int(self.cellwidth * (1 - r2)) + 1
        yend = top + int(self.cellheight * (1 - r2)) + 1

        if not self.selection:

            outl = self.disable_drawing(row, col,self.dx,self.dy)

            if not outl:

                self.draw = True
                outl = 'yellow'

            self.selected_ship.draw(xstart, ystart, xend, yend,row,col,self.dx,self.dy,outl)

        else:

            outl = self.disable_drawing(row, col,self.selected_ship.dx,self.selected_ship.dy)

            if not outl:

                self.draw = True
                outl = 'yellow'

            self.selected_ship.draw(xstart, ystart, xend, yend, row, col, self.selected_ship.dx, self.selected_ship.dy,outl)

    def motion(self,event):

        x = self.canvasx(event.x)  # перевести координати вікна
        y = self.canvasy(event.y)  # у координати canvas
        row = min(int(y) // self.cellheight, self.rows - 1)
        col = min(int(x) // self.cellwidth, self.cols - 1)

        if self.selected_ship:

            self.move_ship(row,col)

    def change_current_ship(self):

        if self.ships[self.current_ship]:

            if self.ships[self.current_ship] > 1:

                self.ships[self.current_ship] -= 1

            else:

                self.ships[self.current_ship] -= 1

                if self.current_ship <= 3:

                    self.current_ship += 1

    def on_click(self,event):

        x = self.canvasx(event.x)  # перевести координати вікна
        y = self.canvasy(event.y)  # у координати canvas
        row = min(int(y) // self.cellheight, self.rows - 1)
        col = min(int(x) // self.cellwidth, self.cols - 1)

        if not self.ready:

            if not self.draw:
                self.parent.bell()
                return

            if self.selected_ship:

                self.change_current_ship()
                self.create_ship(row,col ,self.current_ship,self.ships[self.current_ship])

            else:

                if self.grid[row][col]:

                    self.selected_ship = self.ships_obj[self.grid[row][col]]
                    self.itemconfigure('{}_{}'.format(self.selected_ship.type,self.selected_ship.number),outline='yellow')

                    for cell in self.selected_ship.cells:

                        self.grid[cell[0]][cell[1]] = None

                    self.selection = True
        else:

            if not self.ai:

                self.app.play(row,col,self.name)

            else:

                self.app.root.bell()

    def rotate(self,event):

        if self.selected_ship:

            x = self.canvasx(event.x)  # перевести координати вікна
            y = self.canvasy(event.y)  # у координати canvas
            row = min(int(y) // self.cellheight, self.rows - 1)
            col = min(int(x) // self.cellwidth, self.cols - 1)

            if not self.selection:

                if self.selected_ship.disable_motion(row, col, self.dx * ((-1)) ** (self.c + 1),self.dy * ((-1)) ** self.c):
                    return

            else:

                if self.selected_ship.disable_motion(row, col, self.selected_ship.dx  * ((-1)) ** (self.selected_ship.c + 1),self.selected_ship.dy * ((-1)) ** self.selected_ship.c):
                    return

            self.delete('{}_{}'.format(self.selected_ship.type, self.selected_ship.number))

            key,value = self.selected_ship.main_cell.popitem()
            self.selected_ship.main_cell[key] = value

            _row,_col = key
            x1, y1, x2, y2 = value


            dx = self.dx * ((-1)) ** (self.c + 1)
            dy = self.dy * ((-1)) ** self.c
            _dx = self.selected_ship.dx * ((-1)) ** (self.selected_ship.c + 1)
            _dy = self.selected_ship.dy * ((-1)) ** self.selected_ship.c
            cells = []
            self.selected_ship.cells.clear()

            for i in range(self.selected_ship.type):

                if i == 0:

                    _cell = (row, col)

                else:
                    if not self.selection:

                        if dx == dy:

                            _cell = (row, col + (dx // 30) * i)

                        else:

                            _cell = (row + (dy // 30) * i, col)

                    else:

                        if _dx == _dy:

                            _cell = (row, col + (_dx // 30) * i)

                        else:

                            _cell = (row + (_dy // 30) * i, col)


                cells.append(_cell)


            if not self.selection:

                outl = self.disable_rotation(_row, _col,dx ,dy,cells)

            else:

                outl = self.disable_rotation(_row, _col,_dx,_dy,cells)

            if not outl:

                self.draw = True
                outl = 'yellow'


            for i in range(self.selected_ship.type):

                if i != 0:
                    if not self.selection:

                        if self.dx == self.dy:

                            y1 += self.dy
                            y2 += self.dy

                        else:

                            x1 += self.dx
                            x2 += self.dx

                    else:

                        if self.selected_ship.dx == self.selected_ship.dy:

                            y1 += self.selected_ship.dy
                            y2 += self.selected_ship.dy

                        else:

                            x1 += self.selected_ship.dx
                            x2 += self.selected_ship.dx
                self.selected_ship.cells[cells[i]] = (x1, y1, x2, y2)
                self.create_rectangle(x1, y1, x2, y2, fill='blue',outline = outl,
                                         tag='{}_{}'.format(self.selected_ship.type, self.selected_ship.number))

            if not self.selection:

                self.dx = self.dx * ((-1)) ** (self.c + 1)
                self.dy = self.dy * ((-1)) ** self.c
                self.c += 1
                self.selected_ship.dx = self.dx
                self.selected_ship.dy = self.dy
                self.selected_ship.c += 1

            else:

                self.selected_ship.dx = self.selected_ship.dx * ((-1)) ** (self.selected_ship.c + 1)
                self.selected_ship.dy = self.selected_ship.dy * ((-1)) ** self.selected_ship.c
                self.selected_ship.c += 1


    def disable_drawing(self,row,col,dx,dy):

        for i in range(self.selected_ship.type):

            if i == 0:

                cell = (row, col)

            else:

                if dx == dy:

                    cell = (row, col + (dx // 30) * i)

                else:

                    cell = (row + (dy // 30) * i, col)

            next_cells = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

            for n, m in next_cells:

                if cell[0] + n < 0 or cell[0] + n > 9 or cell[1] + m < 0 or cell[1] + m > 9:

                    continue

                _cell = (cell[0] + n, cell[1] + m)

                if self.grid[_cell[0]][_cell[1]]:

                    self.draw = False
                    return 'red'

    def disable_rotation(self, row, col, dx, dy,cells):

        for cell in cells:

            next_cells = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1) ]

            for n, m in next_cells:

                if cell[0] + n < 0 or cell[0] + n > 9 or cell[1] + m < 0 or cell[1] + m > 9:
                    continue

                _cell = (cell[0] + n, cell[1] + m)

                if self.grid[_cell[0]][_cell[1]]:

                    self.draw = False
                    return 'red'

    def auto_collocation(self):

        for row in range(self.rows):
            for col in range(self.cols):

                self.grid[row][col] = None

        for tag in self.ships_obj:

            self.delete(tag)

        if self.selected_ship:

            self.delete('{}_{}'.format(self.selected_ship.type, self.selected_ship.number))
            self.selected_ship = None

        self.ships_obj.clear()
        self.current_ship = 1
        self.ships = {1: 4, 2: 3, 3: 2, 4: 1}


        while len(self.ships_obj) < 10:

            row = random.randrange(0,10)
            col = random.randrange(0,10)
            i = random.randrange(0,4)
            d_xy = [(30, 30),(-30,30),(-30,-30),(30,-30)]
            dx,dy = d_xy[i]
            xstart, ystart, xend, yend = self.grid_[row][col]
            t = False
            if self.current_ship == 5:
                return

            for j in range(self.current_ship):

                if row + (dy // 30) * j < 0 or row + (dy // 30) * j > 9 or  col + (dx // 30) * j < 0 or  col + (dx // 30) * j > 9:

                    t = True
                    break

                if dx == dy:

                    cell = (row, col + (dx // 30) * j)

                else:

                    cell = (row + (dy // 30) * j, col)

                next_cells = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

                for n, m in next_cells:

                    if cell[0] + n < 0 or cell[0] + n > 9 or cell[1] + m < 0 or cell[1] + m > 9:

                        continue

                    _cell = (cell[0] + n, cell[1] + m)


                    if self.grid[_cell[0]][_cell[1]]:

                        t = True
                        break

            if not t:

                ship = Ship(self.current_ship, self.ships[self.current_ship], self, xstart, ystart, xend - 2, yend - 2,row, col, i, 'black', dx=dx, dy=dy)

                for row, col in ship.cells:

                    self.grid[row][col] = '{}_{}'.format(ship.type,ship.number)


                self.change_current_ship()
                self.ships_obj['{}_{}'.format(ship.type, ship.number)] = ship


    def shoot(self,row,col):

        left = col * self.cellwidth  # лівий верхній кут зображення (х)
        top = row * self.cellheight  # лівий верхній кут зображення (y)
        result = False

        if not self.grid[row][col]:

            r2 = (1 - 0.1) / 2
            xstart = left + int(self.cellwidth * r2) + 1
            ystart = top + int(self.cellheight * r2) + 1
            xend = left + int(self.cellwidth * (1 - r2)) + 1
            yend = top + int(self.cellheight * (1 - r2)) + 1

            self.grid[row][col] = 1

            self.create_oval(xstart, ystart, xend, yend)
            result = False
            return result


        elif self.grid[row][col] == 1:

            return True

        else:

            r2 = (1 - self.ratio) / 2
            xstart = left + int(self.cellwidth * r2) + 1
            ystart = top + int(self.cellheight * r2) + 1
            xend = left + int(self.cellwidth * (1 - r2)) + 1
            yend = top + int(self.cellheight * (1 - r2)) + 1

            if self.ships_obj[self.grid[row][col]].decks >= 1:

                if self.ships_obj[self.grid[row][col]].decks == 1:

                    for cell,coord in self.ships_obj[self.grid[row][col]].cells.items():

                        next_cells = [(0, 1), (0, -1), (1, 0),(-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1) ]

                        for x,y in next_cells:

                            if cell[0] + x > 9 or cell[0] + x < 0 or cell[1] + y > 9 or cell[1] + y < 0:

                                continue

                            if not self.grid[cell[0] + x][cell[1] + y]:

                                self.grid[cell[0] + x][cell[1] + y] = 1
                                c = self.grid_[cell[0] + x][cell[1] + y]

                                self.create_oval(c[0] + 14, c[1] + 14, c[0] + 17,c[1] + 17)
                    result = self.ships_obj[self.grid[row][col]].type
                    del self.ships_obj[self.grid[row][col]]

                else:
                    result = True


                if self.grid[row][col] in self.ships_obj:

                    self.ships_obj[self.grid[row][col]].decks -= 1

                self.grid[row][col] = 1

            self.create_rectangle(xstart, ystart, xend, yend, fill='blue')
            self.create_line(xstart, ystart, xend, yend, fill='red')
            self.create_line(xstart + 30, ystart, xend - 30, yend, fill='red')

            return result


if __name__ == '__main__':
    
    top = Tk()
    gc = Field(top,None,'Field', bordercolor = 'grey',
                    width=300, height=300, bg='white', bd=1)
    gc.auto_collocation()
    gc.pack()
    mainloop()