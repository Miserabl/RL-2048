import pygame 
import random

pygame.init()
font = pygame.font.SysFont('Helvetica', 60)
screen = pygame.display.set_mode((1800,980))
clock = pygame.time.Clock()
running = True
coords = {}
tiles = {
    0: 0, 
    1: 0, 
    2: 0, 
    3: 0,
    4: 0, 
    5: 0, 
    6: 0, 
    7: 0, 
    8: 0, 
    9: 0, 
    10: 0, 
    11: 0, 
    12: 0, 
    13: 0, 
    14: 0, 
    15: 0
}


class tile():
    def __init__(self, coords, tiles, size, value):
        self.value = value
        self.num = random.choice(list(tiles.keys()))
        self.top = coords[self.num][0]
        self.left = coords[self.num][1]
        self.size = size
         
        rect1 = pygame.Rect(self.top, self.left, size, size)
        pygame.draw.rect(screen, ( 238, 228, 218 ), rect1)
        screen.blit(font.render(str(self.value), True, (50,50,50)), (self.top + size/3 + 10, self.left + size/3 - 5 ))
    
    def delete(self, tiles):
        rect1 = pygame.Rect(self.top, self.left, self.size, self.size)
        pygame.draw.rect(screen, "gray", rect1)
        tiles[self.num] = 0

    
    def combine(t1, t2, tiles):
        t2.value *= 2
        t1.delete()
        del t1
    



def setup():
    screen.fill("black")

    start_L = 650
    start_T = 200
    width = 600
    height = 600
    diff = (width - 40)/4
    

    
    rect1 = pygame.Rect(start_L, start_T, width, height)
    pygame.draw.rect(screen, "white", rect1)
    count = 0

    for i in range(4):
        for j in range(4):
            
            rect2 = pygame.Rect(start_L + i * diff + 10 * i, 
                                start_T + j * diff + 10 * j, 
                                diff, 
                                diff)
            
            coords[count] = ((start_L + i * diff + 10 * i,start_T + j * diff + 10 * j))
            count += 1
            
            pygame.draw.rect(screen, "gray", rect2) 
            pygame.draw.line(screen, "black", 
                             (start_L, start_T + (j + 1) * diff + 10 * j + 4), 
                             (start_L + width, start_T + (j + 1) * diff + 10 *  j + 4),
                             width = 10)
        
            
        pygame.draw.line(screen, "black", 
                             (start_L + i * diff + diff + i * 10 + 4, start_T), 
                             (start_L + i * diff + diff + i * 10 + 4, start_T + height),
                             width = 10)
        
    a = tile(coords, tiles, diff, 2)
    print(a.num)
    del tiles[a.num]
    print(tile(coords, tiles, diff, random.choice([2,2,2,2,2,4])).num)




    
    

setup()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
        
                  
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


