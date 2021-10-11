from tkinter import Tk, Button, Frame, Label, Entry, IntVar

"""
	-R = root
	-mgame = main game
"""
R = Tk()
menu = Frame(R)
mgame = Frame(R)
Won = Frame(R)


def click(row, col, board):
    for y, x in zip((row, row+1, row, row-1, row), (col, col, col+1, col, col-1)):
        if (len(board[0]) != x and len(board) != y) and (-1 not in (x, y)):
            if board[y][x].cget("bg") == "#f33":
                board[y][x].config(bg="#33f")
            else:
                board[y][x].config(bg="#f33")
    if all([i.cget("bg") == "#33f" for e in range(len(board)) for i in board[e]]):
        Win(mgame)


def Menu(oldframe=False):
    if oldframe:
        oldframe.forget()
    menu.pack()
    welcome = Label(menu, text="Welcome to this...\n thing?, i guess")
    welcome.config(font=("helvetica", 50))
    welcome.grid(row=0, column=0, columnspan=4, pady=60)
    cvar = IntVar(value=6)
    rvar = IntVar(value=6)
    hlabel = Label(
        menu, text="Rows '2-10' & Columns '2-15' (6 by default) ", font="helvetica 18")
    hlabel.grid(row=1, column=0, columnspan=4, pady=10)
    rlabel = Label(menu, text="Rows:", font="helvetica 12")
    rlabel.grid(row=2, column=0, pady=10, sticky="E")
    rentry = Entry(menu, textvariable=rvar, font="helvetica 12")
    rentry.grid(row=2, column=1, pady=10)
    clabel = Label(menu, text="Columns:", font="helvetica 12")
    clabel.grid(row=2, column=2, sticky="E")
    centry = Entry(menu, textvariable=cvar, font="helvetica 12")
    centry.grid(row=2, column=3, pady=10)
    sbtn = Button(menu, text="START", command=lambda: StartGame(rvar.get(), cvar.get(), menu)
                  if (2 <= rvar.get() <= 10) and (2 <= cvar.get() <= 15) else "")
    sbtn.config(font=("comic sans", 30), bg="#f33")
    sbtn.grid(row=3, column=0, columnspan=4, pady=20)
    R.mainloop()


def StartGame(Row=6, Column=6, oldframe=False):
    if oldframe:
        oldframe.forget()
    for i in mgame.winfo_children():
        i.destroy()
    mgame.pack()
    board = []
    for row in range(Row):
        board.append([])
        for col in range(Column):
            board[row].append(Button(mgame, height=3, width=6, bg="#f33"))
            board[row][col].config(
                command=lambda x=(row, col, board): click(*x))
            board[row][col].grid(row=row, column=col, pady=12, padx=12)
    back = Button(mgame, height=3, width=6, text="Back", font="helvetica 15")
    back.config(command=lambda: Menu(mgame))
    back.grid(row=0, column=col+1)

    R.mainloop()


def Win(oldframe):
    oldframe.forget()
    Won.pack()
    Victory = Label(Won, text="You are a... winner?,\n i guess",
                    font=("helvetica", 40))
    Victory.grid(row=0, column=0, padx=30, pady=40)
    back = Button(Won, text="Back", command=lambda: Menu(
        Won), font=("helvetica", 20), bg="#33f")
    back.grid(row=1, column=0, pady=20, padx=10)


Menu()
