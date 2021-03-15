from tkinter import *

import math

class ConnectFour_GUI():

    GRAY = '#666664'
    window = Tk()
    window_height = 480
    window_width = 640

    def __init__(self, model):
        """
        starts the main render loop
        """
        self.init_window()
        self.init_canvas()
        self.draw_board(self.canvas)
        self.window.mainloop()


    def init_window(self):
        self.window.title("Connect Four")
        self.window.configure(bg=self.GRAY)
        self.window.geometry(f'{self.window_width}x{self.window_height}')

    def init_canvas(self):
        self.canvas = Canvas()
        self.canvas.configure(bg=self.GRAY)
        self.canvas.pack(fill=BOTH, expand=1)

    def draw_piece(self, color, x, y):
        cell_start_x = self.board_start_x + (x * self.cell_width)
        cell_start_y = self.board_start_y + (y * self.cell_height)
        self.canvas.create_oval(
            self.offset_x + cell_start_x,
            self.offset_y + cell_start_y,
            cell_start_x + self.cell_width - self.offset_x,
            cell_start_y + self.cell_height - self.offset_y,
            fill=color
        )

    def handle_click(self, click):
        cell_x_index = math.floor((click.x - self.board_start_x) / self.cell_width)
        cell_y_index = math.floor((click.y - self.board_start_y) / self.cell_height)
        print(f'{cell_x_index}, {cell_y_index}')
        print(f'{click.x}, {click.y}')
        self.draw_piece('yellow', cell_x_index, cell_y_index)


    def draw_board(self, canvas):
        self.board_start_x = self.window_width - (self.window_width * 0.95) 
        self.board_start_y = self.window_height - (self.window_height * 0.95)
        self.board_end_x = self.window_width * 0.95
        self.board_end_y = self.window_height * 0.95
        self.canvas.create_rectangle(
            self.board_start_x,
            self.board_start_y,
            self.board_end_x,
            self.board_end_y,
            outline='black',
            fill='blue',
        )
        self.cell_width = (self.board_end_x - self.board_start_x) / 7
        self.cell_height = (self.board_end_y - self.board_start_y) / 6

        self.offset_x = (self.board_end_x - self.board_start_x) * 0.01
        self.offset_y = (self.board_end_y - self.board_start_y) * 0.01

        for i in range(0, 6):
            for j in range(0, 7):
                cell_start_x = self.board_start_x + (j * self.cell_width) 
                cell_start_y = self.board_start_y + (i * self.cell_height) 
                self.canvas.create_oval(
                    self.offset_x + cell_start_x,
                    self.offset_y + cell_start_y,
                    cell_start_x + self.cell_width - self.offset_x,
                    cell_start_y + self.cell_height - self.offset_y,
                    fill=self.GRAY,
                    tag=f'cell'
                )
                self.canvas.tag_bind(f'cell', '<Button-1>', self.handle_click)