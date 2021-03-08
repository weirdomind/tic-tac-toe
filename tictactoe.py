from tkinter import *

root = Tk()
root.title("Tic-Tac-Toe")

mat = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
]


def someoneWon():
    global mat
    for i in range(len(mat)):
        if (mat[i][0] == mat[i][1] and mat[i][1] == mat[i][2] and mat[i][2] != ""):
            return {"res": True, "name": mat[i][0]}
        if (mat[0][i] == mat[1][i] and mat[1][i] == mat[2][i] and mat[2][i] != ""):
            return {"res": True, "name": mat[0][i]}
    if (mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2] and mat[2][2] != ""):
        return {"res": True, "name": mat[0][0]}
    if (mat[0][2] == mat[1][1] and mat[2][0] == mat[1][1] and mat[1][1] != ""):
        return {"res": True, "name": mat[0][2]}
    return {"res": FALSE, "name": "nobody"}


activePalyer = "X"

finished = False


def changePlayer():
    global activePalyer
    if (activePalyer == "X"):
        activePalyer = "O"
    else:
        activePalyer = "X"


def myfun(number):
    global activePalyer, finished
    if(mat[int((number-(((number-1) % 3)+1))/3)
           ][int((number - 1) % 3)] == "" and not finished):
        buttons[int((number-(((number-1) % 3)+1))/3)
                ][int((number - 1) % 3)].config(text=activePalyer, font="times 12")
        mat[int((number-(((number-1) % 3)+1))/3)
            ][int((number - 1) % 3)] = activePalyer
        changePlayer()
        if (someoneWon()["res"]):
            finished = True
            print(someoneWon()["name"] + " won")


b1 = Button(root, width=20, height=10,
            command=lambda: myfun(1), text=mat[0][0])
b1.grid(row=1, column=1)

b2 = Button(root, width=20, height=10, command=lambda: myfun(2))
b2.grid(row=1, column=2)

b3 = Button(root, width=20, height=10, command=lambda: myfun(3))
b3.grid(row=1, column=3)

b4 = Button(root, width=20, height=10, command=lambda: myfun(4))
b4.grid(row=4, column=1)

b5 = Button(root, width=20, height=10, command=lambda: myfun(5))
b5.grid(row=4, column=2)

b6 = Button(root, width=20, height=10, command=lambda: myfun(6))
b6.grid(row=4, column=3)

b7 = Button(root, width=20, height=10, command=lambda: myfun(7))
b7.grid(row=8, column=1)

b8 = Button(root, width=20, height=10, command=lambda: myfun(8))
b8.grid(row=8, column=2)

b9 = Button(root, width=20, height=10, command=lambda: myfun(9))
b9.grid(row=8, column=3)

buttons = [
    [b1, b2, b3],
    [b4, b5, b6],
    [b7, b8, b9],
]


root.mainloop()
