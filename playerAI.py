#!usr/bin/env python3

'''
    MiniMax Algorithm with alpha-beta pruning:
    - Maximizing Player plays BLACK
    - Minimizing Player plays RED
'''

import math
import random
import os

def create_board():
  '''
    Function that creates the initial board 
    - Using List Comprehension
  '''
  board= [[' ' for i in range(COLS)]for j in range (ROWS)];
  return board
  

os.system("cls")
def colorDisk(disk):
  '''
  coloring each disk using the COLORS dictionary
  '''
  if(disk == 'R'):
    disk =  "\u001b[31mR" + "\u001b[30m" 
  if(disk == 'B'):
    disk =  "\u001b[30mB" 
  return disk      

def print_board(board):
  '''
    Printing the formatted board
    - Using nested for-loop
  '''
  for row in range (ROWS):
    for col in range (COLS):
      if (board[row][col] == ' '):
        print("|_|", end="")
      else:
        print("|" + colorDisk(board[row][col]) + "|", end="")
    print()

def copy_board(board):
  '''
    Creates a temporary board
    Used in minimax
  '''
  temp_board = create_board()

  for row in range(ROWS):
    for col in range(COLS):
      temp_board[row][col] = board[row][col]

  return temp_board


def openRow(board, column):
  ''' 
    Function to check the validity of a chosen column
    - Returns the next open row for a specified column
    - If all rows are taken, returns -1
  '''

  for row in range(ROWS - 1, -1, -1):
    if (board[row][column] == ' '):
      return row
  return -1


def MakeMove(board, row, column, disk):
  '''
    Puts a current disk on the specified position
  '''
  board[row][column] = disk
  return board



def left2right_diagonal_C4(row, col, board, disk):
  '''
    Used in CheckConnect4 Function
    - Checks left to right diagonals
  '''
  if(board[row][col]== disk and board[row-1][col+1]== disk and board[row-2][col+2]== disk and board[row-3][col+3]== disk):
    return True

def right2left_diagonal_C4(row, col, board, disk):
  '''
    Used in CheckConnect4 Function
    - Checks right to left diagonals
  '''
  if(board[row][col]== disk and board[row-1][col-1]== disk and board[row-2][col-2]== disk and board[row-3][col-3]== disk):
    return True

def CheckConnect4(board, disk):
  '''
    Check all the possible positions where Connect 4 could occur:
    - horizontal case
    - vertical case
    - left to right diagonal case (uses left2right_diagonal_C4)
    - right to left diagonal case (uses right2left_diagonal_C4)
  '''

  # Horizontal Case
  for row in range(ROWS):
    for element in range(COLS - 3):
      if(board[row][element]==disk and board[row][element+1]== disk and board[row][element+2]== disk and board[row][element+3]== disk):
        return True

  # Vertical Case
  for row in range(ROWS - 3):
    for element in range(COLS):
      if(board[row][element]==disk and board[row+1][element]== disk and board[row+2][element]== disk and board[row+3][element]== disk):
        return True
  
  # Left to right diagonal Case
  for row in range(3, ROWS):
    for col in range(COLS - 3):
      if left2right_diagonal_C4(row, col, board, disk):
        return True

  # Right to left diagonal Case
  for row in range(3, ROWS):
    for col in range(3, COLS):
      if right2left_diagonal_C4(row, col, board, disk):
        return True

  #If it gets to this point no connect 4
  return False



def left2right_diagonal_C3(row, col, board, disk): 
  '''
    Used in CheckConnect3 Function
    - Checks left to right diagonals
  '''
  if(board[row][col]== disk and board[row-1][col+1]== disk and board[row-2][col+2]== disk):
    return True
 

def right2left_diagonal_C3(row, col, board, disk): 
  '''
    Used in CheckConnect3 Function
    - Checks right to left diagonals
  '''
  if(board[row][col]== disk and board[row-1][col-1]== disk and board[row-2][col-2]== disk):
    return True


def CheckConnect3(board, disk):
  '''
    Check all the possible positions where Connect 3 could occur:
    - horizontal case
    - vertical case
    - left to right diagonal case (uses left2right_diagonal_C3)
    - right to left diagonal case (uses right2left_diagonal_C3)
  '''
  count = 0

  # Horizontal Case
  for row in range(ROWS):
    for element in range(COLS - 3):
      if(board[row][element]==disk and board[row][element+1]== disk and board[row][element+2]== disk and board[row][element+2]== ' '):
        count += 1

  # Vertical Case
  for row in range(ROWS - 3):
    for element in range(COLS):
      if(board[row][element]==disk and board[row+1][element]== disk and board[row+2][element]== disk and board[row+3][element]== ' '):
        count += 1

  # Left to right diagonal Case
  for row in range(2, ROWS):
    for col in range(0, COLS - 2):
      if(left2right_diagonal_C3(row, col, board, disk)):
        count += 1

  # Right to left diagonal Case
  for row in range(2, ROWS):
    for col in range(2, COLS):
      if(right2left_diagonal_C3(row, col, board, disk)):
        count += 1

  # Total number of connect 3
  return count



def left2right_diagonal_C2(row, col, board, disk): 
  '''
    Used in CheckConnect2 Function
    - Checks left to right diagonals
  '''
  if board[row][col]== disk and board[row-1][col+1]== disk:
    return True

def right2left_diagonal_C2(row, col, board, disk): 
  '''
    Used in CheckConnect2 Function
    - Checks right to left diagonals
  '''
  if board[row][col]== disk and board[row-1][col-1]== disk:
    return True

def CheckConnect2(board, disk):
  '''
    Check all the possible positions where Connect 2 could occur:
    - horizontal case
    - vertical case
    - left to right diagonal case (uses left2right_diagonal_C2)
    - right to left diagonal case (uses right2left_diagonal_C2)
  '''
  count = 0

  # Horizontal Case
  for row in range(ROWS):
    for element in range(COLS - 3):
      if(board[row][element]==disk and board[row][element+1]== disk and board[row][element+2]== ' '):
        count += 1

  # Vertical Case
  for row in range(ROWS - 3):
    for element in range(COLS):
      if(board[row][element]==disk and board[row+1][element]== disk and board[row+2][element]== ' '):
        count += 1

  # Left to right diagonal Case
  for row in range(1, ROWS):
    for col in range(0, COLS - 1):
      if(left2right_diagonal_C2(row, col, board, disk)):
        count += 1

  # Right to left diagonal
  for row in range(1, ROWS):
    for col in range(1, COLS):
      if(right2left_diagonal_C2(row, col, board, disk)):
        count += 1

  # Total number of Connect 2
  return count


def utility(board):

  score_AI = 0
  score_Player = 0

  # Checking the score of the center column
  col = COLS // 2
  for row in range(ROWS):
    if (board[row][col] == 'B'):
      score_AI += 3

  # Getting the score for AI
  score_AI += CheckConnect3(board, 'B') * 5
  score_AI += CheckConnect2(board, 'B') * 2


  # Getting the score for the player
  score_Player -= CheckConnect3(board, 'R') * 10000
  score_Player -= CheckConnect2(board, 'R') * 2

  return score_AI + score_Player


def gameover(board):
  return (CheckConnect4(board, 'R') or CheckConnect4(board, 'B'))


# Add the comments to make the code more readable
def minimax(board, depth, alpha, beta, maximizingPlayer):


  ''' Base Case '''

  game_over = gameover(board)

  if depth == 0 or game_over:
    if (game_over):
      if (CheckConnect4(board, 'B')):
        return (None, 10000000)
      else:
        return (None, -10000000)

    else:
      return (None, utility(board))

  #AI's move
  if maximizingPlayer:
    maxEval = -math.inf  
    for column in range(7): #There are only 7 possible moves for the AI
      temp_board = copy_board(board) #Make a temporary board to use as reference
      row = openRow(temp_board, column) #Get the next open row
      if row >= 0:
        temp_board = MakeMove(temp_board, row, column, 'B') #Making a move to the temporary board
        eval = minimax(temp_board, depth - 1, alpha, beta, False)[1] #Leveraging the benefits of recursion to implement the algorithm
        if eval > maxEval:
          maxEval = eval
          move = column
        alpha = max(alpha, maxEval)
        if beta <= alpha: #Tree Pruning occurs in this part
          break
    return move, maxEval
  #Player's move
  else:
    minEval = math.inf 
    for column in range(7):
      temp_board = copy_board(board)
      row = openRow(temp_board, column)
      if row >= 0:
        temp_board = MakeMove(temp_board, row, column, 'R')
        eval = minimax(temp_board, depth - 1, alpha, beta, True)[1]
        if eval < minEval:
          minEval = eval
          move = column
        beta = min(beta, minEval)
        if beta <= alpha:
          break
    return move, minEval





''' Main code starts here '''

# Global Variables
ROWS = 6
COLS = 7

#Determining who's going to start first through a coin toss
coin_toss= random.randint(0, 1)
if (coin_toss == 0):
  turn = 'R'
else:
  turn = 'B'


#Initializing the board
board = create_board()

#Game Introduction
print("CONNECT 4: RED VS BLACK")
print(" ")
print_board(board)
print(" ")

#Variables to keep track of the game:
game_finished = False
round = 0

# Main code
while not game_finished: 

  # Player's turn
  if turn == 'R':

    # Determining the move
    # Getting input from the user
    column = int(input("Player, what column would you like to insert in? ")) - 1
    row = openRow(board, column) #Getting the next available row

    # If the column is full prompt the user to insert another column
    while (row == -1):
        column = int(input(f"Column {column + 1} is taken. Please, Choose another column to play: ")) - 1
        row = openRow(board, column)

    MakeMove(board, row, column, turn)

  # AI's turn
  elif turn == 'B':
    # Call Minimax to choose the best move
    print("AI is making a move:")
    column = minimax(board, 6, -math.inf, math.inf, True)[0]
    row = openRow(board, column)
    MakeMove(board, row, column, turn)

  # Print the board after the move
  print_board(board)
  print()

  # Update Round Count
  round += 1

  # Check if the game is over
  if round == 42 or CheckConnect4(board, turn):
    game_finished= 'true'
    break

  #Changing turns:
  turn= 'R' if turn=='B' else 'B'

if CheckConnect4(board, 'R'):
  print('Player won!')

elif CheckConnect4(board, 'B'):
  print('AI won!')

else:
  print("It's a tie!")
