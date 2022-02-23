board = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
         [0, 1, 0, 0, 0, 4, 0, 0, 0],
         [4, 0, 7, 0, 0, 0, 2, 0, 8],
         [0, 0, 5, 2, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 9, 8, 1, 0, 0],
         [0, 4, 0, 0, 0, 3, 0, 0, 0],
         [0, 0, 0, 3, 6, 0, 0, 7, 2],
         [0, 7, 0, 0, 0, 0, 0, 0, 3],
         [9, 0, 3, 0, 0, 0, 6, 0, 4]]



def printb(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - ')

        for j in range(len(b[i])):
            if j % 3 == 0 and j != 0:
                print('| ',end='')

            if j == 8:
                print(b[i][j])
            else:        
                print(str(b[i][j])+' ',end='')  
          
            
def check(x,y,num):
    for i in range(9):    
        if board [x][i] == num:       
            return False     
    for j in range(9):
        if board [j][y] == num:
            return False
        
    x0 = (y//3) * 3
    y0 = (x//3) * 3

    for i in range(3):
        for j in range(3):       
            if board[y0+i][x0+j] == num:           
                return False
    return True              


def function():
    for j in range(9):
        for i in range(9):       
            if board[j][i] == 0:           
                for n in range(1,10):
                    if check(j,i,n):
                        board[j][i] = n                    
                        function()
                        board[j][i] = 0                    
                return
    printb(board)                       

function()


