import random

board = list(range(0,9))


def show() : 
   print(board[0], '|', board[1], '|',board[2])
   print('----------')
   print(board[3], '|', board[4], '|',board[5])
   print('----------')
   print(board[6], '|', board[7], '|',board[8])

show()

def checkLine(char, spot1, spot2, spot3):
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        return True
        
def checkAll(char):
    if checkLine(char, 0, 1, 2):
        return True
    if checkLine(char, 3, 4, 5):
        return True
    if checkLine(char, 6, 7, 8):
        return True
        
    if checkLine(char, 0, 3, 6):
        return True
    if checkLine(char, 1, 4, 7):
        return True
    if checkLine(char, 2, 5, 8):
        return True
        
    if checkLine(char, 0, 4, 8):
        return True
    if checkLine(char, 2, 4, 6):
        return True
        
    if board[0] == 0 or board[1] == 1 or board[2] == 2 or board[3]==3 or board[4] ==   4 or board[5]==5 or board[6]==6 or board[7]==7 or board[8]==8 :
        return False
    else:
        print('Oops, game is a draw... Try Again?')
    show()
    
 
while True:

  input_ = input("Select a Spot: ")
  input_ = int(input_)
 
  if board[input_] != 'o' and board[input_] != 'x':
      board[input_] = 'o'
      

      if checkAll('o') == True:
          print("~~O WINS~~")
          break;
      
      while True:
          random.seed()  # It gives a random number generator
          computer = random.randint(0,8)
      
          if board[computer] != 'x' and board[computer] != 'o':
              board[computer] = 'x'
              
              if checkAll('x') == True:
                  print("~~X WINS~~")
                  break;
              
              break;

  else:
   print('This spot is taken!')
   
  show()
