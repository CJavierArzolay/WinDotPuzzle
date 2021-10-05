from tkinter import Tk,Button,Frame,Label,Entry,IntVar

"""-R = root \n-mscrn = Main screen \n
-gscrn = Game screen \n-wscrn = Win screen"""
R = Tk()
mscrn = Frame(R)
gscrn = Frame(R)
wscrn = Frame(R)

def click(row,col,board):
	for y,x in zip((row,row+1,row,row-1,row),(col,col,col+1,col,col-1)):
		if (len(board[0]) != x and len(board) != y) and (-1 not in (x,y)):
			if board[y][x].cget("bg") == "#f33":
				board[y][x].config(bg="#33f")
			else:
				board[y][x].config(bg="#f33")
	if all([i.cget("bg") == "#33f" for e in range(len(board)) for i in board[e]]):
		Win(gscrn)

def Menu(oldframe=False):
	if oldframe: oldframe.forget()
	mscrn.pack()
	welcome = Label(mscrn,text="Welcome to this...\n thing?, i guess")
	welcome.config(font=("helvetica",50))
	welcome.grid(row=0,column=0,columnspan=4,pady=60)
	cvar = IntVar(value=6)
	rvar = IntVar(value=6)
	hlabel = Label(mscrn,text="Rows '2-10' & Columns '2-15' (6 by default) "
		,font="helvetica 18")
	hlabel.grid(row=1,column=0,columnspan=4,pady=10)
	rlabel = Label(mscrn,text="Rows:",font="helvetica 12")
	rlabel.grid(row=2,column=0,pady=10,sticky="E")
	rentry = Entry(mscrn,textvariable=rvar,font="helvetica 12")
	rentry.grid(row=2,column=1,pady=10)
	clabel = Label(mscrn,text="Columns:",font="helvetica 12")
	clabel.grid(row=2,column=2,sticky="E")
	centry = Entry(mscrn,textvariable=cvar,font="helvetica 12")
	centry.grid(row=2,column=3,pady=10)
	sbtn = Button(mscrn,text="START",command=lambda:StartGame(rvar.get(),cvar.get(),mscrn)
		if (2 <= rvar.get() <= 10) and (2 <= cvar.get() <= 15) else "")
	sbtn.config(font=("comic sans",30),bg="#f33")
	sbtn.grid(row=3,column=0,columnspan=4,pady=20)
	R.mainloop()

def StartGame(Row=6,Column=6,oldframe = False):
	if oldframe: oldframe.forget()
	for i in gscrn.winfo_children(): i.destroy()
	gscrn.pack()
	board = []
	for row in range(Row):
		board.append([])
		for col in range(Column):
			board[row].append(Button(gscrn,height=3,width=6,bg="#f33"))
			board[row][col].config(command=lambda x=(row,col,board):click(*x))
			board[row][col].grid(row=row,column=col,pady=12,padx=12)
	bkbttn = Button(gscrn, height=3, width=6, text="Back", font="helvetica 15")
	bkbttn.config(command=lambda : Menu(gscrn) )
	bkbttn.grid(row=0,column=col+1)

	R.mainloop()

def Win(oldframe):
	oldframe.forget()
	wscrn.pack()
	Victory = Label(wscrn,text="You are a... winner?,\n i guess", font=("helvetica",40))
	Victory.grid(row=0,column=0,padx=30,pady=40)
	bkbtn = Button(wscrn,text="Back",command=lambda : Menu(wscrn),font=("helvetica",20),bg="#33f")
	bkbtn.grid(row=1,column=0,pady=20,padx=10)

Menu()