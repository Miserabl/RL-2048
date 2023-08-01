import pygame
import random


class Tile:
    def __init__(self, num, size, value, top, left):
        self.value = value
        self.num = num
        self.top = top
        self.left = left
        self.size = size


class Game:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('Helvetica', 60)
        self.font2 = pygame.font.SysFont('Helvetica', 30)
        self.font3 = pygame.font.SysFont('Helvetica', 45)
        self.screen = pygame.display.set_mode((1800, 980))
        self.clock = pygame.time.Clock()
        self.running = True
        self.tiles = {}
        self.start_L = 650
        self.start_T = 200
        self.size_square = 140
        self.size_line = 10
        self.score = 0
        self.colors = {
            2: (238, 228, 218),
            4: (237, 224, 200),
            8: (242, 177, 121),
            16: (242, 177, 121),
            32: (246, 124, 95),
            64: (246, 94, 59),
            128: (237, 207, 114),
            256: (237, 204, 97),
            512: (237, 200, 80),
            1024: (237, 197, 63),
            2048: (237, 194, 46)
        }
        self.reset()
                
        

    def draw(self):
        self.screen.fill("black")

        rect1 = pygame.Rect(self.start_L - 25, self.start_T - 25, self.size_square * 4 + self.size_line * 3 + 50, self.size_square * 4 + self.size_line * 3 + 50)
        pygame.draw.rect(self.screen, (90, 90, 90), rect1)

        rect1 = pygame.Rect(self.start_L - 25, self.start_T - 150, 800, 35)
        pygame.draw.rect(self.screen, (220, 220, 220), rect1)
        self.screen.blit(self.font2.render("Score: " + str(self.score), True, (50, 50, 50)), (self.start_L - 25, self.start_T - 150))

        board = [0] * 16
        for i in range(16):
            row = i // 4
            col = i % 4
            rect1 = pygame.Rect(self.start_L + (self.size_square + self.size_line) * col, self.start_T + (self.size_square + self.size_line) * row, self.size_square, self.size_square)
            pygame.draw.rect(self.screen, (211, 211, 211), rect1)

        for i in self.tiles:
            if self.tiles[i].value in self.colors:
                color = self.colors[self.tiles[i].value]
            else:
                color = (237, 194, 46)
            rect1 = pygame.Rect(self.tiles[i].top, self.tiles[i].left, self.tiles[i].size, self.tiles[i].size)
            pygame.draw.rect(self.screen, color, rect1)
            self.screen.blit(self.font3.render(str(self.tiles[i].value), True, (50, 50, 50)), (self.tiles[i].top + self.size_square // 3 - 15, self.tiles[i].left + self.size_square // 3 - 10))

    def combine(self, t1, t2):
        t2.value *= 2
        del self.tiles[t1.num]
        self.score += t2.value

    def moveup(self):
        var = False
        for i in range(12):
            if i in self.tiles:
                for j in range(i + 4, 16, 4):
                    if j in self.tiles:
                        if self.tiles[i].value == self.tiles[j].value:
                            self.combine(self.tiles[j], self.tiles[i])
                            var = True
                            break
                        else:
                            break

        for i in range(15, 3, -1):
            if i in self.tiles and i - 4 not in self.tiles:
                self.tiles[i - 4] = Tile(i - 4, self.size_square, self.tiles[i].value, self.start_L + (self.size_square + self.size_line) * ((i - 4) % 4), self.start_T + (self.size_square + self.size_line) * ((i - 4) // 4))
                del self.tiles[i]
                var = True

        return var

    def moveright(self):
        var = False
        for i in range(15, -1, -1):
            if i % 4 == 0:
                continue
            if i in self.tiles:
                j = i - 1
                while (j + 1) % 4 != 0:
                    if j in self.tiles:
                        if self.tiles[i].value == self.tiles[j].value:
                            self.combine(self.tiles[j], self.tiles[i])
                            var = True
                            break
                        else:
                            break

                    j -= 1

        for i in range(16):
            if i in self.tiles and i + 1 not in self.tiles and (i + 1) % 4 != 0:
                self.tiles[i + 1] = Tile(i + 1, self.size_square, self.tiles[i].value, self.start_L + (self.size_square + self.size_line) * ((i + 1) % 4), self.start_T + (self.size_square + self.size_line) * ((i + 1) // 4))
                del self.tiles[i]
                var = True

        return var

    def moveleft(self):
        var = False
        for i in range(16):
            if (i + 1) % 4 == 0:
                continue
            if i in self.tiles:
                j = i + 1
                while j % 4 != 0:
                    if j in self.tiles:
                        if self.tiles[i].value == self.tiles[j].value:
                            self.combine(self.tiles[j], self.tiles[i])
                            var = True
                            break
                        else:
                            break
                    j += 1

        for i in range(15, -1, -1):
            if i in self.tiles and i - 1 not in self.tiles and i % 4 != 0:
                self.tiles[i - 1] = Tile(i - 1, self.size_square, self.tiles[i].value, self.start_L + (self.size_square + self.size_line) * ((i - 1) % 4), self.start_T + (self.size_square + self.size_line) * ((i - 1) // 4))
                del self.tiles[i]
                var = True

        return var

    def movedown(self):
        var = False
        for i in range(15, 3, -1):
            if i in self.tiles:
                for j in range(i - 4, -1, -4):
                    if j in self.tiles:
                        if self.tiles[i].value == self.tiles[j].value:
                            self.combine(self.tiles[j], self.tiles[i])
                            var = True
                            break
                        else:
                            break

        for i in range(12):
            if i in self.tiles and i + 4 not in self.tiles:
                self.tiles[i + 4] = Tile(i + 4, self.size_square, self.tiles[i].value, self.start_L + (self.size_square + self.size_line) * ((i + 4) % 4), self.start_T + (self.size_square + self.size_line) * ((i + 4) // 4))
                del self.tiles[i]
                var = True

        return var

    def reset(self):
        self.tiles = {}
        self.score = 0
        avail = [i for i in range(16) if i not in self.tiles]
        num1 = random.choice(avail)
        avail.remove(num1)
        num2 = random.choice(avail)
        val2 = random.choices((2,4),[5,1])[0] 
        self.tiles[num1]= Tile(num1, self.size_square, 2, self.start_L + (self.size_square + self.size_line) * (num1 % 4), self.start_T + (self.size_square + self.size_line) * (num1 // 4))
        self.tiles[num2] = Tile(num2, self.size_square, val2, self.start_L + (self.size_square + self.size_line) * (num2 % 4), self.start_T + (self.size_square + self.size_line) * (num2 // 4))
        self.frame_iteration = 0
        self.running = True

    def get_board_state(self):
        state = [None] * 16
        for i in range(16):
            if i in self.tiles:
                state[i] = self.tiles[i]
        return state
    
    def lose(self, avail):
        #length check
        if len(avail) !=  1:
            return False
        
        #lose check
        check = []
        for i in range(16):
            if i % 4 == 3:
                check = [i - 1, i + 4, i - 4]
            elif i % 4 == 0:
                check = [i + 1, i + 4, i - 4]
            else:
                check = [i + 1, i - 1, i + 4, i - 4]

            check = [x for x in check if (x > -1 and x < 16)]
            for x in check:
                if self.tiles[i].value == self.tiles[x].value:
                    return False

        return True

    def wait(self):
        self.draw()
        pygame.display.flip()
        pygame.time.wait(1000)

    def endgame(self):
        rect1 = pygame.Rect(self.start_L - 25, self.start_T - 25, self.size_square * 4 + self.size_line * 3 + 50, self.size_square * 4 + self.size_line * 3 + 50)
        pygame.draw.rect(self.screen, (80, 80, 80), rect1)
        self.screen.blit(self.font.render("Game Over", True, (50, 50, 50)), (self.start_L + 50, self.start_T + 200))

    def move(self, a):
        # 1 - > left, 2 up, 3 down 4 right
        if a == 1:
            res = self.moveleft()
            self.wait()
            

        elif a == 2:
            res = self.moveup()
            self.wait()
            

        elif a == 3:
            res = self.movedown()
            self.wait()
            
        
        elif a == 4:
            res = self.moveright()
            self.wait()
            
        
        if res:
            avail = [i for i in range(16) if i not in self.tiles]
            num1 = random.choice(avail)
            self.tiles[num1] = Tile(num1, self.size_square, random.choices((2, 4), [9, 1])[0], self.start_L + (self.size_square + self.size_line) * (num1 % 4), self.start_T + (self.size_square + self.size_line) * (num1 // 4))
            self.draw()
            if self.lose(avail):
                self.reset()

   
    def step(self):
            action = random.choice([1,2,3,4])
            self.move(action)
            self.clock.tick(60)
            pygame.display.flip()

   


# Starting the game
if __name__ == "__main__":
    game = Game()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.step()
            print(event)
        
pygame.quit()