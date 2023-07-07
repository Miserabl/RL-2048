import pygame 
import random

pygame.init()
font = pygame.font.SysFont('arial', 50)
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

    def __init__(self, coords, tiles, size):
        self.value = random.choices([2,4], 1, [5,1])
        self.num = random.choices(list(tiles.keys()), 1)
        self.top = coords[self.num][0]
        self.left = coords[self.num][1]
        self.size = size
        del tiles[self.num]
        
        rect1 = pygame.Rect(self.top, self.left, size, size)
        pygame.draw.rect(screen, ( 238, 228, 218 ), rect1)
        screen.blit(font.render(str(self.value), True, (255,0,0)), (self.top + size/3 , self.left + size/3))

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
        
    tile(coords, tiles, diff)
    
    

setup()
print(coords)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
        
                  
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


