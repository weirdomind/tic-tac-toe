# importing stuffs from tkinter.
from tkinter import *
from tkinter import messagebox

# making a root(parent) element.
root = Tk()
root.title("Tic-Tac-Toe")

# default state for our matrix.
# this matrix will help us to check if someone won by providing thevalues of all the boxes.
mat = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
]

# Buttons that can triger an onclick function.


def new_Btns():
    b1 = Button(root, width=20, height=10,
                command=lambda: onClick(1), text=mat[0][0])
    b1.grid(row=1, column=1)

    b2 = Button(root, width=20, height=10, command=lambda: onClick(2))
    b2.grid(row=1, column=2)

    b3 = Button(root, width=20, height=10, command=lambda: onClick(3))
    b3.grid(row=1, column=3)

    b4 = Button(root, width=20, height=10, command=lambda: onClick(4))
    b4.grid(row=4, column=1)

    b5 = Button(root, width=20, height=10, command=lambda: onClick(5))
    b5.grid(row=4, column=2)

    b6 = Button(root, width=20, height=10, command=lambda: onClick(6))
    b6.grid(row=4, column=3)

    b7 = Button(root, width=20, height=10, command=lambda: onClick(7))
    b7.grid(row=8, column=1)

    b8 = Button(root, width=20, height=10, command=lambda: onClick(8))
    b8.grid(row=8, column=2)

    b9 = Button(root, width=20, height=10, command=lambda: onClick(9))
    b9.grid(row=8, column=3)
    # returning a matrix of 3*3 buttons.
    return [
        [b1, b2, b3],
        [b4, b5, b6],
        [b7, b8, b9],
    ]


# reset button.
rsbtn = Button(root, width=10, height=2, command=lambda: reset(), text="RESET")
# showing the reset button.
rsbtn.grid(row=12, column=1)

# When player exits our program using our exit button on close button.


def greet(exited):
    if (exited):
        # if main window was closed create a new window.
        last = Tk()
        last.title("THANKS")  # title for new window.
        # new label created to render on last window.
        thnx = Label(text="Thanks for Trying out my WEIRD App",
                     font="arial 20", width=30, height=10)
        # render that label.
        thnx.grid(row=2, column=2)
        last.mainloop()
    else:
        # if main window was not closed.
        # just make a popup.
        messagebox.showinfo("Thanks",
                            "Thanks for Trying out my WEIRD App")

# exit dialog box.


def myexit():
    global exited
    result = messagebox.askyesno(
        "EXIT", "Do you want to exit the GAME?")  # confirmation for exit.
    if (result):
        greet(False)
        exit()


# exit button.
exitbtn = Button(root, width=10, height=2,
                 command=lambda: myexit(), text="EXIT")
exitbtn.grid(row=12, column=3)

# creating new buttons for player for the first time.
buttons = new_Btns()

# setting default active player.
activePalyer = "X"

# showing the current active player on a label.
currPlayerbtn = Label(root, text="Current Player: "+activePalyer)
currPlayerbtn.grid(row=12, column=2)


finished = False

# checking if someone won or not.


def someoneWon():
    # our matrix and buttons.
    global mat, buttons
    for i in range(len(mat)):
        # checking horizontally.
        if (mat[i][0] == mat[i][1] and mat[i][1] == mat[i][2] and mat[i][2] != ""):
            # filling green bg
            buttons[i][0].config(bg="#0f0")
            buttons[i][1].config(bg="#0f0")
            buttons[i][2].config(bg="#0f0")
            return {"res": True, "name": mat[i][0]}
        # checking vertically.
        if (mat[0][i] == mat[1][i] and mat[1][i] == mat[2][i] and mat[2][i] != ""):
            # filling green bg
            buttons[0][i].config(bg="#0f0")
            buttons[1][i].config(bg="#0f0")
            buttons[2][i].config(bg="#0f0")
            return {"res": True, "name": mat[0][i]}
    # checking one diagonal.
    if (mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2] and mat[2][2] != ""):
        # filling green bg
        buttons[0][0].config(bg="#0f0")
        buttons[1][1].config(bg="#0f0")
        buttons[2][2].config(bg="#0f0")
        return {"res": True, "name": mat[0][0]}
    # checking another diagonal.
    if (mat[0][2] == mat[1][1] and mat[2][0] == mat[1][1] and mat[1][1] != ""):
        # filling green bg
        buttons[0][2].config(bg="#0f0")
        buttons[1][1].config(bg="#0f0")
        buttons[2][0].config(bg="#0f0")
        return {"res": True, "name": mat[0][2]}
    # checking if the match is a TIE.
    tie = True
    for row in mat:
        for ele in row:
            if (ele == ""):
                tie = False
    return {"res": False, "name": "nobody", "tie": tie}

# for toggling player.


def changePlayer():
    global activePalyer
    if (activePalyer == "X"):
        activePalyer = "O"
    else:
        activePalyer = "X"

# for restarting the game.


def reset():
    global mat, buttons, finished, activePalyer
    restart = messagebox.askyesno(
        "RESTART", "Do you want to restart the game?")  # confirmation for restart.
    if (restart):
        # default matrix.
        mat = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]
        # default boxes.
        buttons = new_Btns()
        finished = False
        # default active player.
        activePalyer = "X"

# function to be called when one of the nine boxes is clicked.


def onClick(number):
    # our current player, matrix and buttons.
    global activePalyer, finished, mat, buttons
    # math for finding the index of number(args)
    # mat[int((number-(((number-1) % 3)+1))/3)][int((number - 1) % 3)]

    # checking if the button is pressed first time and the game is not over(win or tie).
    if(mat[int((number-(((number-1) % 3)+1))/3)
           ][int((number - 1) % 3)] == "" and not finished):
        # changing the button's text to the current player's value("X" or "O").
        buttons[int((number-(((number-1) % 3)+1))/3)
                ][int((number - 1) % 3)].config(text=activePalyer, font="times 12")
        # updating the matrix.
        mat[int((number-(((number-1) % 3)+1))/3)
            ][int((number - 1) % 3)] = activePalyer
        changePlayer()  # changing the player
        # updating the label which shows the current player.
        currPlayerbtn.config(text="Current Player: " + activePalyer)

        # checking if someone won
        if (someoneWon()["res"]):
            finished = True
            # popping up a dialog box for the winner.
            messagebox.showinfo("Congratulations",
                                someoneWon()["name"] + " won the match!")
            reset()  # reseting the game.
        #  if the game is a tie.
        elif (someoneWon()["tie"]):
            # popping up a dialog box.
            messagebox.showinfo("Tie",
                                "This match was a TIE")
            reset()  # reseting the game.


# making the window non-resizable.
root.resizable(False, False)
# displaying all stuffs
root.mainloop()

# when the user exits the main window new window will popup to greet.
greet(True)
