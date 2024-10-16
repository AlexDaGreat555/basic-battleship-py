

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
#5 [Check6-1] & #3 [Check6-2] & #3 [Hw6] & #4 [Hw6]
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["rows"] = 10
    data["cols"] = 10
    data["B_Size"] = 500
    data["cell_Size"] = data["B_Size"]//data["rows"]
    data["num_ships"] = 5
    data["com_grid"] = emptyGrid(data["rows"], data["cols"])
    data["user_grid"] = emptyGrid(data["rows"], data["cols"])
    data["temp_Ship"] = []
    data["com_grid"] = addShips(data["com_grid"], data["num_ships"])
    data["num_Ships"] = 0
    data["winner"] = None
    data["max_turns"] = 50
    data["current_turns"] = 0
    


'''
makeView(data, userCanvas, compCanvas)
#6 [Check6-1] & #2 [Check6-2] & #3 [Hw6]
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data,compCanvas,data["com_grid"], False)
    drawGrid(data,userCanvas,data["user_grid"],True)
    drawShip(data,userCanvas, data["temp_Ship"])
    drawGameOver(data,userCanvas)
    


'''
keyPressed(data, events)
#5 [Hw6]
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    if event.keysym == "Return":
        makeModel(data)
    pass


'''
mousePressed(data, event, board)
#5 [Check6-2] & #1 [Hw6] & #3 [Hw6]
Parameters: dict mapping strs to values ; mouse event object ; str
Returns: None
'''
def mousePressed(data, event, board):
    rc = getClickedCell(data,event)
    if board == "user":
        clickUserBoard(data,rc[0],rc[1])
    else:
        if data["num_Ships"] == 5:
            runGameTurn(data,rc[0], rc[1])
            
        
    
    pass

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
#1 [Check6-1]
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    grid = []
    for r in range(rows):
        col_g = []
        for c in range(cols):
            col_g.append(1)
        grid.append(col_g)
        
    return grid


'''
createShip()
#2 [Check6-1]
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    r = random.randrange(1,9)
    c = random.randrange(1,9)
    v_h = random.randrange(0,2)
    center = [r, c]
    ship = []
    if v_h == 0:
        ship.append([r - 1,c])
        ship.append(center)
        ship.append([r + 1,c])
    else:
        ship.append([r,c - 1])
        ship.append(center)
        ship.append([r,c + 1])
        
    return ship


'''
checkShip(grid, ship)
#3 [Check6-1]
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    for i in range(len(ship)):
        r = ship[i][0]
        c = ship[i][1]
        if grid[r][c] != EMPTY_UNCLICKED:
            return False
    return True


'''
addShips(grid, numShips)
#4 [Check6-1]
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    i = 0
    while i < numShips:
        s = createShip()
        if checkShip(grid, s) == True:
            for e in range(len(s)):
                r = s[e][0]
                c = s[e][1]
                grid[r][c] = SHIP_UNCLICKED
            i += 1
            
    return grid


'''
drawGrid(data, canvas, grid, showShips)
#6 [Check6-1] & #1 [Hw6]
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    
    for r in range(data["rows"]):
        top = r * data["cell_Size"]
        bottom = top + data["cell_Size"]
        for c in range(data["cols"]):
            left = c * data["cell_Size"]
            right = left + data["cell_Size"]
            if grid[r][c] == SHIP_UNCLICKED and showShips == True:
                canvas.create_rectangle(left,top,right,bottom, fill = "yellow")
            elif grid[r][c] == SHIP_UNCLICKED and showShips == False:
                canvas.create_rectangle(left,top,right,bottom, fill = "blue")
            elif grid[r][c] == SHIP_CLICKED:
                canvas.create_rectangle(left,top,right,bottom, fill = "red")
            
            elif grid[r][c] == EMPTY_CLICKED:
                canvas.create_rectangle(left,top,right,bottom, fill = "white")
            else:
                canvas.create_rectangle(left,top,right,bottom, fill = "blue")
                
    return

 
### WEEK 2 ###

'''
isVertical(ship)
#1 [Check6-2]
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    rows = [ship[0][0], ship[1][0], ship[2][0]]
    rows.sort()
    center = ship[1]
    if rows[1] - rows[0] != 1 or rows[2] - rows[1] != 1:
        return False
    for i in ship:
        if i[1] != center[1]:
            return False
    return True


'''
isHorizontal(ship)
#1 [Check6-2]
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    cols = [ship[0][1], ship[1][1], ship[2][1]]
    cols.sort()
    center = ship[1]
    if cols[1] - cols[0] != 1 or cols[2] - cols[1] != 1:
        return False
    for i in ship:
        if i[0] != center[0]:
            return False
    return True
    


'''
getClickedCell(data, event)
#2 [Check6-2]
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    row = event.y // data["cell_Size"]
    col = event.x // data["cell_Size"]
    
    return [row,col]

'''
drawShip(data, canvas, ship)
#3 [Check6-2]
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    
    for clicked in ship:
        x1 = clicked[1] * data["cell_Size"]
        y1 = clicked[0] * data["cell_Size"]
        x2 = x1 + data["cell_Size"]
        y2 = y1 + data["cell_Size"]
        canvas.create_rectangle(x1,y1,x2,y2, fill = "white")
    


'''
shipIsValid(grid, ship)
#4 [Check6-2]
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if len(ship) != 3:
        return False
    for coord in ship:
        row = coord[0]
        col = coord[1]
        if grid[row][col] != 1:
            return False
        elif checkShip(grid, ship) != True:
            return False
        elif isVertical(ship) != True and isHorizontal(ship) != True:
            return False
    return True


'''
placeShip(data)
#4 [Check6-2]
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    if shipIsValid(data["user_grid"], data["temp_Ship"]) == True:
        for coord in data["temp_Ship"]:
            row = coord[0]
            col = coord[1]
            data["user_grid"][row][col] = SHIP_UNCLICKED
            
        data["num_Ships"] += 1
        data["temp_Ship"] = []
    else:
        print("Error your ship is not valid! Try Again")
        data["temp_Ship"] = []
        



'''
clickUserBoard(data, row, col)
#4 [Check6-2]
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if data["num_Ships"] == 5:
        return
    if [row,col] in data["temp_Ship"]:
        return
    else:
        data["temp_Ship"] += [[row,col]]
    if len(data["temp_Ship"]) == 3:    
        placeShip(data)
    if data["num_Ships"] == 5:
        print("You can start playing the game!")
        


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
#1 [Hw6] & #3 [Hw6]
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    if board[row][col] == SHIP_UNCLICKED:
        board[row][col] = SHIP_CLICKED
    elif board[row][col] == EMPTY_UNCLICKED:
        board[row][col] = EMPTY_CLICKED
    game_state = isGameOver(board)
    if game_state == True:
        data["winner"] = board

    
        
    


'''
runGameTurn(data, row, col)
#1 [Hw6] & #2 [Hw6] & #4 [Hw6]
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    if data["com_grid"][row][col] == SHIP_CLICKED or data["com_grid"][row][col] == EMPTY_CLICKED:
        return
    else:
        updateBoard(data,data["com_grid"],row,col,"user")
        com_guess = getComputerGuess(data["user_grid"])
        updateBoard(data,data["user_grid"],com_guess[0],com_guess[1],"com")
        data["current_turns"] += 1
        print(data["current_turns"])
    if data["current_turns"] == data["max_turns"]:
        data["winner"] = "draw"
        

        



'''
getComputerGuess(board)
#2 [Hw6]
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    coord = 0
    i = 0
    row = 0
    col = 0
    while i < 1:
        row = random.randint(0,9)
        col = random.randint(0,9)
        coord = board[row][col]
        if coord == SHIP_UNCLICKED or coord == EMPTY_UNCLICKED:
            i += 1
    return [row,col]


'''
isGameOver(board)
#3 [Hw6]
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    for coord in board:
        if SHIP_UNCLICKED in coord:
            return False
    return True


'''
drawGameOver(data, canvas)
#3 [Hw6] & #4 [Hw6] & #5 [Hw6]
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    if data["winner"] == data["com_grid"]:
        canvas.create_text(data["B_Size"]//2,data["B_Size"]//2, text = "You Won!!!:)", fill = "light Green", font = ('Ziglets 80 bold'))
        canvas.create_text(data["B_Size"]//2,data["B_Size"]//2 + 50, text = "Press 'Enter' to restart", fill = "light Green", font = ('Ziglets 30 bold'))
    elif data["winner"] == data["user_grid"]:
        canvas.create_text(data["B_Size"]//2,data["B_Size"]//2, text = "You Lost :( Lol", fill = "dark Red", font = ('Ziglets 75 bold'))
        canvas.create_text(data["B_Size"]//2,data["B_Size"]//2 + 50, text = "Press 'Enter' to restart", fill = "dark Red", font = ('Ziglets 30 bold'))
    elif data["winner"] == "draw":
        canvas.create_text(data["B_Size"]//2,data["B_Size"]//2, text = "This Game is a Draw :/", fill = "pink", font = ('Ziglets 50 bold'))
        canvas.create_text(data["B_Size"]//2,data["B_Size"]//2 + 50, text = "Press 'Enter' to restart", fill = "pink", font = ('Ziglets 30 bold'))


    


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
    
