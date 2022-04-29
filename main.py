from tkinter import *
from pandas import ExcelFile
from cell import Cell
import settings
import utils

if __name__ == '__main__':
    root = Tk()
    #Override window settings
    root.configure(bg = "black")
    root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
    root.title('Minesweeper Game')
    root.resizable(False, False)

    top_frame = Frame(
        root,
        bg='black',
        width=settings.WIDTH,
        height=utils.height_prc(25)
    )
    top_frame.place(x=0,y=0)

    left_frame = Frame(
        root,
        bg='black',
        width = utils.width_prc(25),
        height = utils.height_prc(75)
    )
    left_frame.place(x=0, y=utils.height_prc(25))

    center_frame = Frame(
        root,
        bg = 'black',
        width = utils.width_prc(75),
        height = utils.height_prc(75)
    )
    center_frame.place(
        x = utils.width_prc(25), 
        y=utils.height_prc(25)
    )

    def destroyer(event):
        root.destroy()

    restart_btn = utils.create_restart_btn(top_frame)
    restart_btn.bind('<Button-1>', destroyer)

    for x in range(settings.GRID_SIZE):
        for y in range(settings.GRID_SIZE):
            c = Cell(x,y)
            c.create_btn_object(center_frame)
            c.cell_btn_object.grid(
                column = x,
                row = y
            )

    Cell.create_cell_count_label(left_frame)
    Cell.cell_count_label_object.place(
        x=5,
        y=0
    )

    Cell.randomize_mines()
    #Run the window
    root.mainloop()
