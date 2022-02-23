import pygame
pygame.init()


white  = (255, 255, 255)
black = (0, 0, 0)
width = 630
height = width
display = pygame.display.set_mode((width,height))
block = width // 9
display.fill(white)

board = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
         [0, 1, 0, 0, 0, 4, 0, 0, 0],
         [4, 0, 7, 0, 0, 0, 2, 0, 8],
         [0, 0, 5, 2, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 9, 8, 1, 0, 0],
         [0, 4, 0, 0, 0, 3, 0, 0, 0],
         [0, 0, 0, 3, 6, 0, 0, 7, 2],
         [0, 7, 0, 0, 0, 0, 0, 0, 3],
         [9, 0, 3, 0, 0, 0, 6, 0, 4]]

backup = board         


def draw_grid():
    for i in range(0,width,block):
        pygame.draw.line(display,black, (i,0), (i,height),4 if i % 3 == 0 else 1)
    for j in range(0,height,block):
        pygame.draw.line(display,black, (0,j), (width,j),4 if j % 3 == 0 else 1)
    pygame.display.update()

def blit_board(board):
    for j in range(len(board)):
        for i in range(len(board[j])):
            if board[j][i] != 0:
                space = (block/100 *30)
                x = i*block + space
                y = j*block
                font = pygame.font.SysFont('arial', int((block/100)*80))
                text = font.render(str(board[j][i]), True ,black)
                display.blit(text,(x,y))
    pygame.display.update()   
blit_board(board)                         
draw_grid()
    
#this fuction is for printing the whole board in the output section and practically useless while the having the ui.   
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

triggered = 0
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
    blit_board(board)
                         

while True:
    for event in pygame.event.get():
        pygame.display.set_caption('Press Space To See The Solution'.center(60,'='))
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                triggered+=1
                if triggered % 2 != 0:
                    function()
                else:
                    display.fill(white)
                    draw_grid()
                    blit_board(backup)




