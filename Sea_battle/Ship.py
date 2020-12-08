class Ship:
    '''Клас корабель, який прив'язано до клітинки поля.

    '''

    def __init__(self, type, number, parent, xstart, ystart, xend, yend, row, col,c,outl='red',fill='blue',dx=30,dy=30):

        self.type = type
        self.decks = type
        self.number = number
        self.cells = {}
        self.parent = parent
        self.main_cell = {(row,col):(xstart, ystart, xend, yend)}
        self.dx = dx
        self.dy = dy
        self.c = c

        for part in range(self.type):

            self.cells[(row, col)] = (xstart, ystart, xend, yend)
            parent.create_rectangle(xstart, ystart, xend, yend, fill=fill,outline=outl,
                                    tag='{}_{}'.format(self.type, self.number))

            if self.dx == self.dy and self.dx > 0:

                col += 1
                xstart += self.dx
                xend += self.dx

            elif self.dx == self.dy and self.dx < 0:

                col -= 1
                xstart += self.dx
                xend += self.dx

            elif self.dx != self.dy and self.dy > 0:

                row += 1
                ystart += self.dy
                yend += self.dy

            elif self.dx != self.dy and self.dy < 0:

                row -= 1
                ystart += self.dy
                yend += self.dy

    def draw(self,xstart, ystart, xend, yend,row,col,dx, dy,outl):

        self.cells.clear()
        self.dx = dx
        self.dy = dy

        if self.disable_motion(row,col,dx,dy):

            return

        self.parent.delete('{}_{}'.format(self.type, self.number))

        for i in range(self.type):

            if i == 0:

                _cell = (row, col)

                self.main_cell = {}
                self.main_cell[_cell] = (xstart, ystart, xend, yend)

            else:

                if dx == dy:
                    _cell = (row, col + (dx // 30) * i)
                else:
                    _cell = (row + (dy // 30) * i, col)

            self.cells[_cell] = (xstart, ystart, xend, yend)
            self.parent.create_rectangle(xstart, ystart, xend, yend, fill='blue',outline=outl,
                                         tag='{}_{}'.format(self.type, self.number))

            if dx == dy:

                xstart += dx
                xend += dx

            else:

                ystart += dy
                yend += dy

    def disable_motion(self,row,col,dx,dy):

        for i in range(self.type):

            if i == 0:

                _cell = (row, col)

            else:

                if dx == dy:
                    _cell = (row, col + (dx // 30) * i)
                else:
                    _cell = (row + (dy // 30) * i, col)

            if _cell[0] < 0 or _cell[0] > 9 or _cell[1] < 0 or _cell[1] > 9:

                return True

        return False