#!usr/bin/env python3

'''
Player VS Player
'''

import random

def printBoard(board, ROWS, COLS):
    for row in range (ROWS):
      for col in range (COLS):
        if (board[row][col] == ' '):
            print("|_|", end="")
        else:
          print("|" + board[row][col] + "|", end="")
      print()

def left2right_diagonal(row, col, board, disk): #part of Check_Connect4
  if(board[row][col]== disk and board[row-1][col+1]== disk and board[row-2][col+2]== disk and board[row-3][col+3]== disk):
    return True
  
def right2left_diagonal(row, col, board, disk): #part of Check_Connect4
  if(board[row][col]== disk and board[row-1][col-1]== disk and board[row-2][col-2]== disk and board[row-3][col-3]== disk):
    return True


def CheckConnect4(board, disk):

  disk = 'R'if disk=='red' else 'B'

  #Checking if 4 disks are connected in the horizontally
  for row in range(rows):
    for col in range(cols-3):
      if(board[row][col]==disk and board[row][col+1]== disk and board[row][col+2]== disk and board[row][col+3]== disk):
        print("Connect 4!!")
        return True

  #Checking if 4 disks are connected in the vertically
  for row in range(rows-3):
    for col in range(cols):
      if(board[row][col]==disk and board[row+1][col]== disk and board[row+2][col]== disk and board[row+3][col]== disk):
        print("Connect 4!!")
        return True

  #Checking if 4 disks are connected in the diagonally (one way)
  for row in range(3,6):
    for col in range(0,4):
      if(left2right_diagonal(row, col, board, disk)):
        print("Connect 4!!")
        return True

  #Checking if 4 disks are connected in the diagonally (other way)
  for row in range(3,6):
    for col in range(3,7):
      if(right2left_diagonal(row, col, board, disk)):
        print("Connect 4!!")
        return True


  #If it gets to this point no 
  return False





'''
Main Code
'''

#Initialize a 2D array of 6x7 chars:
rows, cols= (6, 7)
board= [[' ' for i in range(cols)]for j in range (rows)]; #initializing an array of empty strings called board

#Initializing variables
keep_going='true'
game_finished='false'
round=0

# Dictionary to keep track of the rows available for every column
'''  
    Initial value is the lowest row = 5 
    Structure Col: OpenRow
'''
NextOpenRow = {i:5 for i in range(cols)}

#Determining who's going to start first through a coin toss
coin_toss= random.randint(0, 1)
if (coin_toss == 0):
  turn = 'red'
else:
  turn = 'black'

#Game Introduction
print("CONNECT 4: RED VS BLACK")
print(" ")
printBoard(board, rows, cols)
print(" ")


while(game_finished == 'false'): 

  #Determining the move:
  columnInsert = int(input(f"{turn}, what column would you like to insert in? "))
  startRow = NextOpenRow[columnInsert - 1]

  #If the column is filled up:
  while (startRow == -1):
      columnInsert = int(input(f"Column {columnInsert} is taken. Please, Choose another column to play: "))
      startRow = NextOpenRow[columnInsert - 1]

  #Executing the move:
  if(turn == 'red'):

    board[startRow][columnInsert - 1] = 'R'
    NextOpenRow[columnInsert - 1] -= 1

  elif(turn == 'black'):

    board[startRow][columnInsert - 1] = 'B'
    NextOpenRow[columnInsert - 1] -= 1

  printBoard(board, rows, cols)

  #Round 2
  round= round+1

  #Finish Game:
  if round == 42 or CheckConnect4(board, turn):
    game_finished= 'true'

  #Changing turns:
  turn= 'red' if turn=='black' else 'black'
