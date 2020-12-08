from Field import *
from tkinter import *
from tkinter.messagebox import *
from AI import *
import time

FIELD_WIDTH = FIELD_HEIGHT = 300

class Application:

    def __init__(self,ai=False):

        self.root = Tk()
        self.i = 0
        self.ai = ai
        self.nextTurn = 'First'
        self.make_widgets()
        self.create_menu()

        if ai:

            self.computer = Ai(self.field_2, self, self.b_ready_2,self.b_auto_2)

        #mainloop()

    def make_widgets(self):

        self.root.title('Sea battle')

        self.f_sea_fields = Frame(self.root)


        self.f_field_1 = Frame(self.f_sea_fields)

        if not self.ai:

            self.field_1 = Field(self,self.f_field_1,'First',width=FIELD_WIDTH,height=FIELD_HEIGHT,bg='white', bd=1)
            self.field_1.pack(side=TOP,pady=5)

        else:

            self.field_1 = Field(self, self.f_field_1, 'First',ai=True, width=FIELD_WIDTH, height=FIELD_HEIGHT, bg='white',bd=1)
            self.field_1.pack(side=TOP, pady=5)


        self.f_ready_1 = Frame(self.f_field_1)

        self.label_1 = Label(self.f_ready_1,text = 'Player 1')
        self.label_1.pack(side=LEFT,pady=5,padx=10)
        self.b_ready_1 = Button(self.f_ready_1, text='Start')
        self.b_ready_1.bind('<Button-1>',lambda event: self.hide_ships(self.field_1,self.b_ready_1,self.b_auto_1))
        self.b_ready_1.pack(side=RIGHT, padx=5, pady=5)
        self.b_auto_1 = Button(self.f_ready_1, text='Auto', command=self.field_1.auto_collocation)
        self.b_auto_1.pack(side=RIGHT, padx=5, pady=5)

        self.f_ready_1.pack(side=TOP,pady=5,padx=10)

        self.f_field_1.pack(side=LEFT,padx = 10,pady=5)


        self.f_field_2 = Frame(self.f_sea_fields)

        if not self.ai:

            self.field_2 = Field(self,self.f_field_2,'Second', width=FIELD_WIDTH, height=FIELD_HEIGHT, bg='white', bd=1)
            self.field_2.pack(side=TOP, pady=5)

        else:

            self.field_2 = Field(self, self.f_field_2, 'Second',p=False, width=FIELD_WIDTH, height=FIELD_HEIGHT, bg='white',bd=1)
            self.field_2.pack(side=TOP, pady=5)

        self.f_ready_2 = Frame(self.f_field_2)

        self.label_2 = Label(self.f_ready_2, text='Player 2')
        self.label_2.pack(side=LEFT, pady=5, padx=10)
        self.b_ready_2 = Button(self.f_ready_2, text='Start')
        self.b_ready_2.bind('<Button-1>', lambda event: self.hide_ships(self.field_2,self.b_ready_2,self.b_auto_2))
        self.b_ready_2.pack(side=RIGHT, padx=5, pady=5)
        self.b_auto_2 = Button(self.f_ready_2, text='Auto',command=self.field_2.auto_collocation)
        self.b_auto_2.pack(side=RIGHT, padx=5, pady=5)

        self.f_ready_2.pack(side=TOP, pady=5, padx=10)

        self.f_field_2.pack(side=LEFT,padx = 10,pady=5)


        self.f_sea_fields.pack(side=LEFT,padx=5,pady=10)



        self.f_info = Frame(self.root)

        self.currentTurn = Label(self.f_info, text='', fg='red', font=('arial', 16, 'bold'))
        self.currentTurn.pack(side=TOP, padx=5)


        self.f_score = Frame(self.f_info)


        Label(self.f_score,text='Scores:').pack(side=TOP,padx = 5)

        self.score_list_1 = Frame(self.f_score)

        Label(self.score_list_1, text='Player 1:').pack(side=TOP, padx=5)
        self.list_player_1 = Field(self, self.score_list_1, '1st',rows = 7,cols = 6,p = False,width=120, height=140,bg='white', bd=1)
        self.list_player_1.pack(side=TOP,padx=10)

        self.score_list_1.pack(side=LEFT)


        self.score_list_2 = Frame(self.f_score)

        Label(self.score_list_2, text='Player 2:').pack(side=TOP, padx=5)
        self.list_player_2 = Field(self, self.score_list_2, '2st', rows=7, cols=6, p=False, width=120, height=140,bg='white', bd=1)
        self.list_player_2.pack(side=TOP,padx=10)

        self.score_list_2.pack(side=LEFT)


        self.f_score.pack(side=TOP,pady = 5)


        self.f_buttons = Frame(self.f_info)
        self.f_buttons.pack(side=TOP,pady = 10)


        self.f_info.pack(side=TOP,padx=5,pady=37)

    def open_menu(self):

        for x in self.root.winfo_children():

            x.destroy()

        menu = Main_menu(self.root)


    def create_menu(self):

        self.menu  = Menu(self.root)
        self.menubar = Menu(self.menu,tearoff=0)

        self.menubar.add_command(label="New game", command=self.new_game)
        self.menubar.add_separator()
        self.menubar.add_command(label="Main menu", command=self.open_menu)
        self.menubar.add_separator()
        self.menubar.add_command(label="Exit",command=self.root.quit)
        self.menu.add_cascade(label="Menu", menu=self.menubar)
        self.root.config(menu=self.menu)


    def hide_ships(self,field,button1,button2):

        if not field.selected_ship and not field.selection:

            for ship in field.ships_obj:

                field.delete(ship)

            field.ready = True

            button1.destroy()
            button2.destroy()
            self.i += 1

            if self.i == 2:

                self.field_2['highlightbackground'] = 'red'
                self.currentTurn['text'] = 'Current turn: {}'.format('Player 1')

                self.b_surrender = Button(self.f_buttons,width=38,height=2, text='Give up', command=self.give_up)
                self.b_surrender.pack(side=LEFT, padx=5, pady=5)

                self.coord = {}

                self.coord[4] = (110, 10)
                self.coord[3] = (90, 50)
                self.coord[2] = (70, 90)
                self.coord[1] = (50, 130)

                Ship(4, 0, self.list_player_1, 1, 1, 21, 21, 0, 0, 0, None, dx=20, dy=20)
                self.list_player_1.create_text(91, 9, text='x', font=('arial', 12, 'italic'))
                self.list_player_1.create_text(110, 10, text='0', font=('arial', 12, 'italic'),tags='s_4')
                Ship(3, 0, self.list_player_1, 1, 41, 21, 61, 2, 0, 0, None, dx=20, dy=20)
                self.list_player_1.create_text(71, 49, text='x', font=('arial', 12, 'italic'))
                self.list_player_1.create_text(90, 50, text='0', font=('arial', 12, 'italic'),tags='s_3')
                Ship(2, 0, self.list_player_1, 1, 81, 21, 101, 4, 0, 0, None, dx=20, dy=20)
                self.list_player_1.create_text(51, 89, text='x', font=('arial', 12, 'italic'))
                self.list_player_1.create_text(70, 90, text='0', font=('arial', 12, 'italic'),tags='s_2')
                Ship(1, 0, self.list_player_1, 1, 121, 21, 141, 6, 0, 0, None, dx=20, dy=20)
                self.list_player_1.create_text(31, 129, text='x', font=('arial', 12, 'italic'))
                self.list_player_1.create_text(50, 130, text='0', font=('arial', 12, 'italic'),tags='s_1')

                Ship(4, 0, self.list_player_2, 1, 1, 21, 21, 0, 0, 0, None, dx=20, dy=20)
                self.list_player_2.create_text(91, 9, text='x', font=('arial', 12, 'italic'))
                self.list_player_2.create_text(110, 10, text='0', font=('arial', 12, 'italic'),tags='s_4')
                Ship(3, 0, self.list_player_2, 1, 41, 21, 61, 2, 0, 0, None, dx=20, dy=20)
                self.list_player_2.create_text(71, 49, text='x', font=('arial', 12, 'italic'))
                self.list_player_2.create_text(90, 50, text='0', font=('arial', 12, 'italic'),tags='s_3')
                Ship(2, 0, self.list_player_2, 1, 81, 21, 101, 4, 0, 0, None, dx=20, dy=20)
                self.list_player_2.create_text(51, 89, text='x', font=('arial', 12, 'italic'))
                self.list_player_2.create_text(70, 90, text='0', font=('arial', 12, 'italic'),tags='s_2')
                Ship(1, 0, self.list_player_2, 1, 121, 21, 141, 6, 0, 0, None, dx=20, dy=20)
                self.list_player_2.create_text(31, 129, text='x', font=('arial', 12, 'italic'))
                self.list_player_2.create_text(50, 130, text='0', font=('arial', 12, 'italic'),tags='s_1')

    def shows_ships(self,field):

        for ship in field.ships_obj.values():

            key, value = ship.main_cell.popitem()
            row,col = key
            xstart, ystart, xend, yend = value
            ship.draw(xstart, ystart, xend, yend,row,col,ship.dx,ship.dy,'black')

    def play(self,row,col,field):

        if self.field_1.ready and self.field_2.ready and field != self.nextTurn:

            if self.nextTurn == 'First':

                shot = self.field_2.shoot(row,col)

                if not shot:

                    self.nextTurn = 'Second'
                    self.field_2['highlightbackground'] = 'blue'
                    self.field_1['highlightbackground'] = 'red'
                    self.currentTurn['text'] = 'Current turn: {}'.format('Player 2')

                    if self.ai:

                        _row,_col = self.computer.shoot(self.field_1.grid)
                        self.play(_row, _col,'First')



                else:

                    if not isinstance(shot, bool):

                        self.field_2.current_ships[shot] += 1
                        self.list_player_1.itemconfig('s_{}'.format(str(shot)),text=str(self.field_2.current_ships[shot]))

                    if not self.field_2.ships_obj:

                        self.shows_ships(self.field_1)
                        self.game_over('Player 1')
                        return



            else:

                shot = self.field_1.shoot(row, col)

                if not shot:

                    self.nextTurn = 'First'
                    self.field_1['highlightbackground'] = 'blue'
                    self.field_2['highlightbackground'] = 'red'
                    self.currentTurn['text'] = 'Current turn: {}'.format('Player 1')

                else:

                    if not isinstance(shot, bool):

                        self.field_1.current_ships[shot] += 1
                        self.list_player_2.itemconfig('s_{}'.format(str(shot)),text=str(self.field_1.current_ships[shot]))

                        if self.ai:

                            self.computer.destroyed.clear()

                    else:

                        if self.ai:

                            self.computer.destroyed.append((row, col))

                    if not self.field_1.ships_obj:

                        self.shows_ships(self.field_2)
                        self.game_over('Player 2')
                        return

                    if self.ai:

                        _row, _col = self.computer.shoot(self.field_1.grid)
                        self.play(_row, _col, 'First')



        else:

            self.root.bell()


    def game_over(self,winner):

        if askokcancel('Game over','         {} won!\n      Start new game?'.format(winner)):

            self.new_game()

        else:

           self.root.destroy()

    def give_up(self):

       if askokcancel('Game over','         {} gave up!\n      Start new game?'.format('Player 2' if self.nextTurn == 'Second' else 'Player 1')):

           self.new_game()

       else:

          self.root.destroy()

    def new_game(self):

        for x in self.root.winfo_children():

            x.destroy()

        self.nextTurn = 'First'
        self.i = 0

        self.make_widgets()
        self.create_menu()

        if self.ai:

            self.computer = Ai(self.field_2, self, self.b_ready_2, self.b_auto_2)



class Main_menu:

    def __init__(self,root=Tk()):

        self.root = root
        self.root.title('Sea battle')
        self.background = Field('as',self.root, 'main',p=False, width=540, height=495, bg='white',bd=1,rows=11,cols=12,highlightbackground='pink',grid='pink')
        self.background.pack(side=TOP)

        self.ship = Ship(2, 0, self.background, 46, 90, 91, 136, 2, 2, 1,'black',dx=45,dy=-45)
        self.ship_ = Ship(2, 1, self.background, 451, 405, 496, 451, 7, 8,'black',dx=45,dy=-45)

        self.ship1 = Ship(4, 0, self.background, 181, 136, 226, 181, 3, 4,1,dx=45,dy=45,outl='white',fill='yellow')
        self.background.create_text(270, 157, text='Single player',fill='pink', font=('arial', 20, 'italic'),tags='Single')

        self.ship2 = Ship(4, 1, self.background, 181, 226, 226, 271, 5, 4,1,dx=45,dy=45,outl='white',fill='yellow')
        self.background.create_text(270, 247, text='Two players',fill='pink', font=('arial', 20, 'italic'),tags='Two')

        self.ship3 = Ship(4, 2, self.background, 181, 316, 226, 361, 7, 4,1,dx=45,dy=45,outl='white',fill='yellow')
        self.background.create_text(268, 337, text='Exit',fill='pink', font=('arial', 20, 'italic'),tags='Exit')

        self.dx,self.dy,self.dx_,self.dy_ = 0,45,0,-45
        self.CURRENT = 1
        self.PREVIOUS = 0

        self.background.bind('<Motion>', self.motion_handler)
        self.background.bind('<Button-1>', self.key_handler)

        self.move()
        self.clipping()

        mainloop()

    def move(self):

        if self.background.coords('2_0')[1] >= 450:

            self.dx = 45
            self.dy = 0
            xstart, ystart, xend, yend = self.background.coords('2_0')
            self.ship.draw(xstart, ystart - 45, xend, yend - 45, 4, 4, 45, 45, 'black')

        elif self.background.coords('2_0')[1] <= 0:

            self.dx = -45
            self.dy = 0
            xstart, ystart, xend, yend = self.background.coords('2_0')
            self.ship.draw(xstart, ystart+45, xend, yend+45, 4, 4, -45, -45, 'black')


        elif self.background.coords('2_0')[0] <= 90:

            self.dx = 0
            self.dy = 45
            xstart, ystart, xend, yend = self.background.coords('2_0')
            self.ship.draw(xstart, ystart, xend, yend, 4, 4, 45, -45, 'black')

        elif self.background.coords('2_0')[0] >= 450:

            self.dx = 0
            self.dy = -45
            xstart, ystart, xend, yend = self.background.coords('2_0')
            self.ship.draw(xstart, ystart, xend, yend, 4, 4, -45, 45, 'black')

        if self.background.coords('2_1')[1] >= 450:

            self.dx_ = 45
            self.dy_ = 0
            xstart, ystart, xend, yend = self.background.coords('2_1')
            self.ship_.draw(xstart, ystart - 45, xend, yend - 45, 4, 4, 45, 45, 'black')

        elif self.background.coords('2_1')[1] <= 0:

            self.dx_ = -45
            self.dy_ = 0
            xstart, ystart, xend, yend = self.background.coords('2_1')
            self.ship_.draw(xstart, ystart+45, xend, yend+45, 4, 4, -45, -45, 'black')


        elif self.background.coords('2_1')[0] <= 90:

            self.dx_ = 0
            self.dy_ = 45
            xstart, ystart, xend, yend = self.background.coords('2_1')
            self.ship_.draw(xstart, ystart, xend, yend, 4, 4, 45, -45, 'black')

        elif self.background.coords('2_1')[0] >= 450:

            self.dx_ = 0
            self.dy_ = -45
            xstart, ystart, xend, yend = self.background.coords('2_1')
            self.ship_.draw(xstart, ystart, xend, yend, 4, 4, -45, 45, 'black')

        self.background.move('2_0',self.dx,self.dy)
        self.background.move('2_1', self.dx_, self.dy_)
        self.background.itemconfig('2_0',fill=random.choice(['red','blue','yellow','pink']))
        self.background.itemconfig('2_1', fill=random.choice(['red', 'blue', 'yellow', 'pink']))

        self.root.after(60, self.move)

    def clipping(self):

        if self.CURRENT == 1:

            self.background.itemconfig('4_0', fill='#dae2d0')
            self.background.itemconfig('Single', font=('arial', 20, 'bold italic'))
            self.background.itemconfig('Two', fill='white', font=('arial', 20, 'italic'))
            self.background.itemconfig('Exit', fill='white', font=('arial', 20, 'italic'))
            self.background.itemconfig('4_1', fill='pink')
            self.background.itemconfig('4_2', fill='pink')
            self.CURRENT = 2

        elif self.CURRENT == 2:

            self.background.itemconfig('4_0', fill='pink')
            self.background.itemconfig('4_1', fill='#dae2d0')
            self.background.itemconfig('Single', fill='white', font=('arial', 20, 'italic'))
            self.background.itemconfig('Two', font=('arial', 20, 'bold italic'))
            self.background.itemconfig('Exit', fill='white', font=('arial', 20, 'italic'))
            self.background.itemconfig('4_2', fill='pink')
            self.CURRENT = 3

        elif self.CURRENT == 3:

            self.background.itemconfig('4_0', fill='pink')
            self.background.itemconfig('4_1', fill='pink')
            self.background.itemconfig('4_2', fill='#dae2d0')
            self.background.itemconfig('Single', fill='white', font=('arial', 20, 'italic'))
            self.background.itemconfig('Two', fill='white', font=('arial', 20, 'italic'))
            self.background.itemconfig('Exit', font=('arial', 20, 'bold italic'))
            self.CURRENT = 1

        self.root.after(377, self.clipping)

    def motion_handler(self,event):

        if event.x >= 181 and event.x <= 360 and event.y >= 138 and event.y <= 180:

            self.CURRENT = 0
            self.PREVIOUS = 1
            self.background.itemconfig('4_0', fill='#dae2d0')
            self.background.itemconfig('Single', font=('arial', 20, 'bold italic'))
            self.background.itemconfig('Two', fill='white', font=('arial', 20, 'italic'))
            self.background.itemconfig('Exit', fill='white', font=('arial', 20, 'italic'))
            self.background.itemconfig('4_1', fill='pink')
            self.background.itemconfig('4_2', fill='pink')

        elif event.x >= 181 and event.x <= 360 and event.y >= 228 and event.y <= 270:

            self.CURRENT = 0
            self.PREVIOUS = 2
            self.background.itemconfig('4_0', fill='pink')
            self.background.itemconfig('4_1', fill='#dae2d0')
            self.background.itemconfig('Single', fill='white', font=('arial', 20, 'italic'))
            self.background.itemconfig('Two', font=('arial', 20, 'bold italic'))
            self.background.itemconfig('Exit', fill='white', font=('arial', 20, 'italic'))
            self.background.itemconfig('4_2', fill='pink')

        elif event.x >= 181 and event.x <= 360 and event.y >= 318 and event.y <= 360:

            self.CURRENT = 0
            self.PREVIOUS = 3
            self.background.itemconfig('4_0', fill='pink')
            self.background.itemconfig('4_1', fill='pink')
            self.background.itemconfig('4_2', fill='#dae2d0')
            self.background.itemconfig('Single', fill='white', font=('arial', 20, 'italic'))
            self.background.itemconfig('Two', fill='white', font=('arial', 20, 'italic'))
            self.background.itemconfig('Exit', font=('arial', 20, 'bold italic'))

        else:

            if self.PREVIOUS != 0:

                self.CURRENT = self.PREVIOUS
                self.PREVIOUS = 0

    def key_handler(self,event):

        if event.x >= 181 and event.x <= 360 and event.y >= 138 and event.y <= 180:

            self.root.destroy()
            app = Application(ai=True)

        elif event.x >= 181 and event.x <= 360 and event.y >= 228 and event.y <= 270:

            self.root.destroy()
            app = Application()

        elif event.x >= 181 and event.x <= 360 and event.y >= 318 and event.y <= 360:

            self.root.quit()



if __name__ == '__main__':

    menu = Main_menu()

