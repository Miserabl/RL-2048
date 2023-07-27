import pygame
import random

pygame.init()
font = pygame.font.SysFont('Helvetica', 60)
font2 = pygame.font.SysFont('Helvetica', 30)
font3 = pygame.font.SysFont('Helvetica', 45)
screen = pygame.display.set_mode((1800,980))
clock = pygame.time.Clock()
running = True
tiles = {}
start_L = 650
start_T = 200
size_square = 140
size_line = 10
score = 0 

colors = {2:( 238, 228, 218 ), 4: (237, 224, 200), 8: (242, 177, 121), 16: (242, 177, 121), 32 : (246, 124, 95),  64:(246, 94, 59), 128: (237, 207, 114), 256: (237, 204, 97), 512:(237, 200, 80), 1024: (237, 197, 63), 2048: (237, 194, 46)  }

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
        if tiles[i].value in colors:
            color = colors[tiles[i].value]
        else:
            color = (237, 194, 46) 
        rect1 = pygame.Rect(tiles[i].top, tiles[i].left, tiles[i].size, tiles[i].size)
        pygame.draw.rect(screen, color, rect1)
        screen.blit(font3.render(str(tiles[i].value), True, (50,50,50)), (tiles[i].top + size_square/3 - 15, tiles[i].left + size_square/3 - 10 ))
            
    

def combine(t1, t2):
    t2.value *= 2
    del tiles[t1.num]
    global score 
    score += t2.value

def moveup():
    var = False
    for i in range(12):
        if i in tiles:
            for j in range(i + 4, 16, 4):
                if j in tiles:
                        if tiles[i].value == tiles[j].value:
                            combine(tiles[j], tiles[i])
                            var = True
                            break
                        else:
                            break
            


    for i in range(15 , 3  , -1):              
            if i in tiles and i - 4 not in tiles:
                tiles[i - 4] = tile(i - 4, size_square, tiles[i].value, start_L + (size_square + size_line) * ((i-4) % 4), start_T + (size_square + size_line) * ((i-4) // 4))
                del tiles[i]
                var = True

    for i in range(15 , 3  , -1):              
            if i in tiles and i - 4 not in tiles:
                tiles[i - 4] = tile(i - 4, size_square, tiles[i].value, start_L + (size_square + size_line) * ((i-4) % 4), start_T + (size_square + size_line) * ((i-4) // 4))
                del tiles[i]
                var = True

    for i in range(15 , 3  , -1):              
            if i in tiles and i - 4 not in tiles:
                tiles[i - 4] = tile(i - 4, size_square, tiles[i].value, start_L + (size_square + size_line) * ((i-4) % 4), start_T + (size_square + size_line) * ((i-4) // 4))
                del tiles[i]
                var = True
    
    return var


def moveright():
    var = False
    for i in range(15, -1, -1):
        if i % 4 == 0:
            continue
        if i in tiles:
            j = i  - 1
            while (j + 1) % 4 != 0:
                if j in tiles:
                    if tiles[i].value == tiles[j].value:
                        combine(tiles[j], tiles[i])
                        var = True
                        break
                    else:
                        break

                j -= 1
    
    for i in range(16):
        if i in tiles and i + 1 not in tiles and ( i + 1) % 4 != 0:
            tiles[i + 1] = tile(i + 1, size_square, tiles[i].value, start_L + (size_square + size_line) * ((i + 1) % 4), start_T + (size_square + size_line) * ((i + 1) // 4))
            del tiles[i]
            var  = True
    for i in range(16):
        if i in tiles and i + 1 not in tiles and ( i + 1) % 4 != 0:
            tiles[i + 1] = tile(i + 1, size_square, tiles[i].value, start_L + (size_square + size_line) * ((i + 1) % 4), start_T + (size_square + size_line) * ((i + 1) // 4))
            del tiles[i]
            var  = True
    for i in range(16):
        if i in tiles and i + 1 not in tiles and ( i + 1) % 4 != 0:
            tiles[i + 1] = tile(i + 1, size_square, tiles[i].value, start_L + (size_square + size_line) * ((i + 1) % 4), start_T + (size_square + size_line) * ((i + 1) // 4))
            del tiles[i]
            var  = True
    
    return var







def moveleft():
    var = False
    for i in range(16):
        if ( i + 1) % 4 == 0:
            continue
        if i in tiles:
            j = i + 1
            while (j % 4 != 0):
                if j in tiles:
                    if tiles[i].value == tiles[j].value:
                            combine(tiles[j], tiles[i])
                            var = True
                            break
                    else:
                        break
                j += 1
    
    for i in range(15, -1 , -1):
        if i in tiles and i - 1 not in tiles and i % 4 != 0:
            tiles[i - 1] = tile(i - 1, size_square, tiles[i].value, start_L + (size_square + size_line) * ((i - 1) % 4), start_T + (size_square + size_line) * ((i - 1) // 4))
            del tiles[i]
            var = True
    
    for i in range(15, -1 , -1):
        if i in tiles and i - 1 not in tiles and i % 4 != 0:
            tiles[i - 1] = tile(i - 1, size_square, tiles[i].value, start_L + (size_square + size_line) * ((i - 1) % 4), start_T + (size_square + size_line) * ((i - 1) // 4))
            del tiles[i]
            var = True

    for i in range(15, -1 , -1):
        if i in tiles and i - 1 not in tiles and i % 4 != 0:
            tiles[i - 1] = tile(i - 1, size_square, tiles[i].value, start_L + (size_square + size_line) * ((i - 1) % 4), start_T + (size_square + size_line) * ((i - 1) // 4))
            del tiles[i]
            var = True
    
    return var

def movedown():
    var = False
    for i in range(15, 3, -1):
        if i in tiles:
            for j in range(i - 4, -1, -4):
                if j in tiles:
                    if tiles[i].value == tiles[j].value:
                        combine(tiles[j], tiles[i])
                        var = True
                        break
                    else:
                        break
    
    for i in range(12):    
        if i in tiles and i + 4 not in tiles:
                tiles[i + 4] = tile(i + 4, size_square, tiles[i].value, start_L + (size_square + size_line) * ((i+4) % 4), start_T + (size_square + size_line) * ((i +4) // 4))
                del tiles[i]
                var = True
    
    for i in range(12):    
        if i in tiles and i + 4 not in tiles:
                tiles[i + 4] = tile(i + 4, size_square, tiles[i].value, start_L + (size_square + size_line) * ((i+4) % 4), start_T + (size_square + size_line) * ((i +4) // 4))
                del tiles[i]
                var = True
    
    for i in range(12):    
        if i in tiles and i + 4 not in tiles:
                tiles[i + 4] = tile(i + 4, size_square, tiles[i].value, start_L + (size_square + size_line) * ((i+4) % 4), start_T + (size_square + size_line) * ((i +4) // 4))
                del tiles[i]
                var = True
    
    return var


        
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
        print(check)
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



def wait():
    draw()
    pygame.display.flip()
    pygame.time.wait(50)


def endgame():
    rect1 = pygame.Rect(start_L - 25, start_T - 25, size_square * 4 + size_line * 3 + 50, size_square * 4 + size_line * 3 + 50)
    pygame.draw.rect(screen, (80,80,80), rect1)
    screen.blit(font.render("Game Over", True, (50,50,50)), (start_L + 50,  start_T + 200))
    
    



gameover = False

while running:
  
    if not gameover:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    res = moveright()
                    wait()
                    if res:
                        avail = [i for i in range(16) if i not in tiles]
                        num1 = random.choice(avail)
                        tiles[num1] = tile(num1, size_square, random.choices((2,4),[9,1])[0], start_L + (size_square + size_line) * (num1 % 4), start_T + (size_square + size_line) * (num1 // 4))
                        draw()
                        if len(avail) == 1 and lose():
                            gameover = True
                    else:
                        continue

                elif event.key == pygame.K_LEFT:
                    res = moveleft()
                    wait()
                    if res:
                        avail = [i for i in range(16) if i not in tiles]
                        num1 = random.choice(avail)
                        tiles[num1] = tile(num1, size_square, random.choices((2,4),[9,1])[0], start_L + (size_square + size_line) * (num1 % 4), start_T + (size_square + size_line) * (num1 // 4))
                        draw()
                        if len(avail) == 1 and lose():
                            gameover = True
                    else:
                        continue
                    

                elif event.key == pygame.K_UP:
                    res = moveup()
                    wait()
                    if res:
                        avail = [i for i in range(16) if i not in tiles]
                        num1 = random.choice(avail)
                        tiles[num1]= tile(num1, size_square, random.choices((2,4),[9,1])[0], start_L + (size_square + size_line) * (num1 % 4), start_T + (size_square + size_line) * (num1 // 4))
                        draw()
                        if len(avail) == 1 and lose():
                            gameover = True
                    else:
                        continue

                elif event.key == pygame.K_DOWN:
                    res = movedown()
                    wait()
                    if res:
                        avail = [i for i in range(16) if i not in tiles]
                        num1 = random.choice(avail)
                        tiles[num1]= tile(num1, size_square, random.choices((2,4),[9,1])[0], start_L + (size_square + size_line) * (num1 % 4), start_T + (size_square + size_line) * (num1 // 4))
                        draw()

                    else:
                        if len(avail) == 1 and lose():
                            gameover = True
                        else:
                            continue

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    
    


    
    clock.tick(60)
    
    draw()
    if gameover:
        endgame()
    pygame.display.flip()

    
pygame.quit()

 




  