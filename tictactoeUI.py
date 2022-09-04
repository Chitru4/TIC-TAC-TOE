from tkinter import *              #MADE BY CHITRAKSH KUMAR
import tictactoeVSUI

board = [
             [' ',' ',' '],
             [' ',' ',' '],
             [' ',' ',' ']
            ] 

root = Tk()
root.title("TIC TAC TOE")

def numberadd(index):
    global board
    index -= 1
    if(index<3):
        i = 0
        j = index
    elif(index<6):
        i = 1
        j = index - 3 
    elif(index<9):
        i = 2 
        j = index - 6
    if board[i][j] != ' ':
        return

    var[index+1].set(" X ")
    board[i][j] = 'X' 
    index,board = tictactoeVSUI.main(index,list(board))
    board[i][j] = 'X' 
    if(index<3):
        i = 0
        j = index
    elif(index<6):
        i = 1
        j = index - 3 
    elif(index<9):
        i = 2 
        j = index - 6 
    board[i][j] = 'O'
    index += 1
    var[index].set(" O ")


var = [0]*10

for i in range(10):
    var[i] = StringVar()
    var[i].set("    ")

onebutton = Button(root , textvariable = var[1] , command = lambda: numberadd(1) , font = "12" ,padx = "10", pady = "10").grid(row=1,column=0)
twobutton = Button(root , textvariable = var[2] , command = lambda: numberadd(2), font = "12" ,padx = "10", pady = "10").grid(row=1,column=1)
threebutton = Button(root , textvariable = var[3] , command = lambda: numberadd(3) , font = "12" ,padx = "10", pady = "10").grid(row=1,column=2)
fourbutton = Button(root , textvariable = var[4] , command = lambda: numberadd(4) , font = "12" ,padx = "10", pady = "10").grid(row=2,column=0)
fivebutton = Button(root , textvariable = var[5] , command = lambda: numberadd(5) , font = "12" ,padx = "10", pady = "10").grid(row=2,column=1)
sixbutton = Button(root , textvariable = var[6] , command = lambda: numberadd(6) , font = "12" ,padx = "10", pady = "10").grid(row=2,column=2)
sevenbutton = Button(root , textvariable = var[7] , command = lambda: numberadd(7) , font = "12" ,padx = "10", pady = "10").grid(row=3,column=0)
eightbutton = Button(root , textvariable = var[8] , command = lambda: numberadd(8) , font = "12" ,padx = "10", pady = "10").grid(row=3,column=1)
ninebutton = Button(root , textvariable = var[9] , command = lambda: numberadd(9) , font = "12" ,padx = "10", pady = "10").grid(row=3,column=2)

root.mainloop()