board = [
         [0,3,0,0,0,0,0,0,5],
         [8,0,9,3,0,0,4,0,0],
         [0,0,0,0,0,0,0,0,2],
         [0,0,0,0,0,1,0,0,0],
         [0,9,1,2,4,0,0,0,0],
         [0,0,0,0,0,5,0,6,7],
         [4,1,0,7,0,9,8,0,0],
         [0,0,0,0,0,2,0,0,3],
         [7,6,0,0,8,0,9,0,0],
        ]

def print_board(board):
    xline = "-"*6+"+"+"-"*6+"+"+"-"*6
    
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print(xline)
        for j in range(len(board[i])):
            if j%3==0 and j!=0:
                print("|",end="")
            if j==8:
                print(board[i][j])
            else:
                print(f"{board[i][j]} ",end="")
                
def is_valid(board,num,pos):
    
    #rows
    for i in range(len(board[pos[0]])):
        if board[pos[0]][i] == num and i!=pos[1]:
            return False
        
    #columns
    for i in range(len(board)):
        if board[i][pos[1]] == num and i!=pos[0]:
            return False
        
    #boxes
    x0=(pos[1]//3)*3
    y0=(pos[0]//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if board[y0+i][x0+j] == num and (i,j)!=pos:
                return False
            
    return True
        
def is_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==0:
                return (i,j)
            
    return False

def solve(board):
    
    if not is_empty(board):
        print_board(board)

    
    else:
        pos = is_empty(board)
        for i in range(1,10):
            if is_valid(board,i,pos):
                board[pos[0]][pos[1]]=i
                solve(board)
                board[pos[0]][pos[1]]=0