import random
import time

class Ai:
    def __init__(self,field,main,button1,button2):

        self.field = field
        self.main = main
        self.field.auto_collocation()
        self.main.hide_ships(self.field,button1,button2)
        self.destroyed = []

    def shoot(self,battle_field):
        self.main.root.update()
        time.sleep(1)

        if not self.destroyed:
            while True:
                row = random.randrange(0,10)
                col = random.randrange(0, 10)

                if battle_field[row][col] != 1:
                    return row,col
        else:
            while True:
                if len(self.destroyed) == 1:
                    x = random.choice((0,1,-1))

                    if x == 0:
                        y = random.choice((1,-1))
                    else:
                        y = 0

                    row = self.destroyed[0][0] + y
                    col = self.destroyed[0][1] + x

                    if row < 10 and row > -1 and col < 10 and col > -1 and battle_field[row][col] != 1:
                        return row,col

                else:
                    row = 0
                    col = 0

                    for i,cell in enumerate(self.destroyed):
                        if i == 0:
                            row = cell[0]
                            col = cell[1]
                        else:
                            _row, _col = self.destroyed[-1]

                            if cell[0] == row:
                                if _col > col :
                                    if _col + 1 < 10 and battle_field[row][_col + 1] != 1:
                                        return row,_col + 1
                                    elif col - 1 > -1 and battle_field[row][col - 1] != 1:
                                        return row, col - 1
                                else:
                                    if _col - 1 > -1 and battle_field[row][_col - 1] != 1:
                                        return row, _col - 1
                                    elif col + 1 < 10 and battle_field[row][col + 1] != 1:
                                        return row, col + 1
                            elif cell[1] == col:
                                if _row > row :
                                    if _row + 1 < 10 and battle_field[_row + 1][col] != 1:
                                        return _row + 1,col
                                    elif row - 1 > -1 and battle_field[row - 1][col] != 1:
                                        return row - 1, col
                                else:
                                    if _row - 1 > -1 and battle_field[_row - 1][col] != 1:
                                        return _row - 1, col
                                    elif row + 1 < 10 and battle_field[row + 1][col] != 1:
                                        return row + 1, col




