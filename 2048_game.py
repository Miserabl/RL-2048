import pygame
import random

pygame.init()
font = pygame.font.SysFont('Helvetica', 60)
font2 = pygame.font.SysFont('Helvetica', 30)
screen = pygame.display.set_mode((1800,980))
clock = pygame.time.Clock()
running = True
tiles = {}
start_L = 650
start_T = 200
size_square = 140
size_line = 10
score = 0 



class tile():
    def __init__(self, num, size, value, top, left):
        self.value = value
        self.num = num
        self.top = top
        self.left = left
        self.size = size
       
    
   
    
   
    



def draw():
    screen.fill("black")


    rect1 = pygame.Rect(start_L - 25, start_T - 25, size_square * 4 + size_line * 3 + 50, size_square * 4 + size_line * 3 + 50)
    pygame.draw.rect(screen, (90, 90, 90), rect1)
    
    rect1 = pygame.Rect(start_L - 25, start_T -  150, 800, 35)
    pygame.draw.rect(screen, (220,220,220), rect1)
    screen.blit(font2.render("Score: " + str(score), True, (50,50,50)), (start_L - 25,  start_T -  150))
    

    board = [0] * 16
    for i in range(16):
        row = i // 4
        col = i % 4
        rect1 = pygame.Rect(start_L + (size_square + size_line) * col, start_T + (size_square + size_line) * row, size_square, size_square)
        pygame.draw.rect(screen, (211, 211, 211) , rect1)
    
    
    
    for i in tiles:
        rect1 = pygame.Rect(tiles[i].top, tiles[i].left, tiles[i].size, tiles[i].size)
        pygame.draw.rect(screen, ( 238, 228, 218 ), rect1)
        screen.blit(font.render(str(tiles[i].value), True, (50,50,50)), (tiles[i].top + size_square/3 + 10, tiles[i].left + size_square/3 - 5 ))
            
    

def combine(t1, t2):
    t2.value *= 2
    del tiles[t1.num]
    global score 
    score += t2.value

def moveup():
    for i in range(15, 3, -1):
        if i in tiles:
            if (i - 4) in tiles:
                if tiles[i].value == tiles[i-4].value:
                    combine(tiles[i], tiles[i - 4])
            else:
                tiles[i - 4] = tile(i - 4, size_square, tiles[i].value, start_L + (size_square + size_line) * ((i-4) % 4), start_T + (size_square + size_line) * ((i-4) // 4))
                del tiles[i]
                
                

def moveright():
    for i in range(16):
        if (i + 1) % 4 == 0 or i not in tiles:
            continue
        
        if i + 1 in tiles:
            if tiles[i].value == tiles[i + 1].value:
                    combine(tiles[i], tiles[i + 1])
        else:
            tiles[i + 1] = tile(i + 1, size_square, tiles[i].value, start_L + (size_square + size_line) * ((i + 1) % 4), start_T + (size_square + size_line) * ((i + 1) // 4))
            del tiles[i]

def moveleft():
    for i in range(15, -1 , -1):
        if i % 4 == 0 or i not in tiles:
            continue
        
        if (i - 1) in tiles:
            if tiles[i].value == tiles[i - 1].value:
                    combine(tiles[i], tiles[i - 1])
        else:
            tiles[i - 1] = tile(i - 1, size_square, tiles[i].value, start_L + (size_square + size_line) * ((i - 1) % 4), start_T + (size_square + size_line) * ((i - 1) // 4))
            del tiles[i]

def movedown():
    for i in range(12):
        if i in tiles:
            if (i + 4) in tiles:
                if tiles[i].value == tiles[i + 4].value:
                    combine(tiles[i], tiles[i + 4])
            else:
                tiles[i + 4] = tile(i + 4, size_square, tiles[i].value, start_L + (size_square + size_line) * ((i+4) % 4), start_T + (size_square + size_line) * ((i +4) // 4))
                del tiles[i]


        
def lose():
    check = []
    for i in range(16):
        if i % 4 == 3:
            check = [i - 1, i + 4, i - 4]
        elif i % 4 == 0:
            check = [i + 1, i + 4, i - 4]
        else:
           check = [i + 1, i - 1, i + 4, i - 4]

        check = [ x for x in check if (x > -1 and x < 16)]
        
        for x in check:
           if tiles[i].value == tiles[x].value:
                return False
    

    return True
        
            
       

        
avail = [i for i in range(16) if i not in tiles]
num1 = random.choice(avail)
avail.remove(num1)
num2 = random.choice(avail)
val2 = random.choices((2,4),[5,1])[0]
    
tiles[num1]= tile(num1, size_square, 2, start_L + (size_square + size_line) * (num1 % 4), start_T + (size_square + size_line) * (num1 // 4))
tiles[num2] = tile(num2, size_square, val2, start_L + (size_square + size_line) * (num2 % 4), start_T + (size_square + size_line) * (num2 // 4))












while running:
  
    avail = [i for i in range(16) if i not in tiles]
    if len(avail) == 0 and lose():
        running = False
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveright()
                
                num1 = random.choice(avail)
                tiles[num1] = tile(num1, size_square, 2, start_L + (size_square + size_line) * (num1 % 4), start_T + (size_square + size_line) * (num1 // 4))
                
                draw()

            elif event.key == pygame.K_LEFT:
                moveleft()
                num1 = random.choice(avail)
                a = tile(num1, size_square, 2, start_L + (size_square + size_line) * (num1 % 4), start_T + (size_square + size_line) * (num1 // 4))
                tiles[num1] = a
                draw()

            elif event.key == pygame.K_UP:
                moveup()
                num1 = random.choice(avail)
                a = tile(num1, size_square, 2, start_L + (size_square + size_line) * (num1 % 4), start_T + (size_square + size_line) * (num1 // 4))
                tiles[num1] = a
                draw()

            elif event.key == pygame.K_DOWN:
                movedown()
                num1 = random.choice(avail)
                a = tile(num1, size_square, 2, start_L + (size_square + size_line) * (num1 % 4), start_T + (size_square + size_line) * (num1 // 4))
                tiles[num1] = a
                draw()

    
    

    
    clock.tick(60)
    draw()
    pygame.display.flip()
    
pygame.quit()

 




  