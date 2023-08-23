

board={1:" ",2:" ",3:" ",
       4:" ",5:" ",6:" ",
       7:" ",8:" ",9:" "}

def showboard():
    print(board[1],"|",board[2],"|",board[3])
    print("--+---+--")
    print(board[4],"|",board[5],"|",board[6])
    print("--+---+--")
    print(board[7],"|",board[8],"|",board[9])
    
def checkfordraw():
    for i in board.values():
        if i==" ":
            return False
    return True 

def check_for_win(player):
    #rows condition
    if board[1]==board[2] and board[1] == board[3] and board[1] == player:
        return True  
    elif board[4]==board[5] and board[4] == board[6] and board[4] == player:
        return True  
    elif board[7]==board[8] and board[7] == board[9] and board[7] == player:
        return True 
 #column condition
    elif board[1]==board[4] and board[1] == board[7] and board[1] == player:
        return True  
    elif board[2]==board[5] and board[2] == board[8] and board[2] == player:
        return True  
    elif board[3]==board[6] and board[3] == board[9] and board[3] == player:
        return True 
    
     #diagonal  condition
    elif board[1]==board[5] and board[1] == board[9] and board[1] == player:
        return True 
    elif board[3]==board[5] and board[3] == board[7] and board[3] == player:
        return True   
    
    else:
        return False  

def insert(player,position):
    if board[position] == " ":
        board[position]=player
        showboard()
        if check_for_win(player):
            print(player,' is Winner')
            quit()
        
        if checkfordraw():
            print("Game Draw")
            quit()
    else:
        print("Position already occupied")
        position = int(input("Enter new position"))
        insert(player,position)

showboard()
player1="X"
player2="O"

while True :
    print(player1,"chance")
    position=int(input("Enter position(1-9) : "))
    insert(player1,position)
    print(player2,"chance")
    position=int(input("Enter position(1-9) : "))
    insert(player2,position)