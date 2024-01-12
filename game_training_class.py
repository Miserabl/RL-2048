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
        self.font = pygame.font.SysFont("Helvetica", 60)
        self.font2 = pygame.font.SysFont("Helvetica", 30)
        self.font3 = pygame.font.SysFont("Helvetica", 45)
        self.screen = pygame.display.set_mode((1800, 980))
        self.clock = pygame.time.Clock()
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
            2048: (237, 194, 46),
        }
        # self.reset()

    def draw(self):
        self.screen.fill("black")

        rect1 = pygame.Rect(
            self.start_L - 25,
            self.start_T - 25,
            self.size_square * 4 + self.size_line * 3 + 50,
            self.size_square * 4 + self.size_line * 3 + 50,
        )
        pygame.draw.rect(self.screen, (90, 90, 90), rect1)

        rect1 = pygame.Rect(self.start_L - 25, self.start_T - 150, 800, 35)
        pygame.draw.rect(self.screen, (220, 220, 220), rect1)
        self.screen.blit(
            self.font2.render("Score: " + str(self.score), True, (50, 50, 50)),
            (self.start_L - 25, self.start_T - 150),
        )

        board = [0] * 16
        for i in range(16):
            row = i // 4
            col = i % 4
            rect1 = pygame.Rect(
                self.start_L + (self.size_square + self.size_line) * col,
                self.start_T + (self.size_square + self.size_line) * row,
                self.size_square,
                self.size_square,
            )
            pygame.draw.rect(self.screen, (211, 211, 211), rect1)

        for i in self.tiles:
            if self.tiles[i].value in self.colors:
                color = self.colors[self.tiles[i].value]
            else:
                color = (237, 194, 46)
            rect1 = pygame.Rect(
                self.tiles[i].top,
                self.tiles[i].left,
                self.tiles[i].size,
                self.tiles[i].size,
            )
            pygame.draw.rect(self.screen, color, rect1)
            self.screen.blit(
                self.font3.render(str(self.tiles[i].value), True, (50, 50, 50)),
                (
                    self.tiles[i].top + self.size_square // 3 - 15,
                    self.tiles[i].left + self.size_square // 3 - 10,
                ),
            )

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
                self.tiles[i - 4] = Tile(
                    i - 4,
                    self.size_square,
                    self.tiles[i].value,
                    self.start_L + (self.size_square + self.size_line) * ((i - 4) % 4),
                    self.start_T + (self.size_square + self.size_line) * ((i - 4) // 4),
                )
                del self.tiles[i]
                var = True

        for i in range(15, 3, -1):
            if i in self.tiles and i - 4 not in self.tiles:
                self.tiles[i - 4] = Tile(
                    i - 4,
                    self.size_square,
                    self.tiles[i].value,
                    self.start_L + (self.size_square + self.size_line) * ((i - 4) % 4),
                    self.start_T + (self.size_square + self.size_line) * ((i - 4) // 4),
                )
                del self.tiles[i]
                var = True

        for i in range(15, 3, -1):
            if i in self.tiles and i - 4 not in self.tiles:
                self.tiles[i - 4] = Tile(
                    i - 4,
                    self.size_square,
                    self.tiles[i].value,
                    self.start_L + (self.size_square + self.size_line) * ((i - 4) % 4),
                    self.start_T + (self.size_square + self.size_line) * ((i - 4) // 4),
                )
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
                self.tiles[i + 1] = Tile(
                    i + 1,
                    self.size_square,
                    self.tiles[i].value,
                    self.start_L + (self.size_square + self.size_line) * ((i + 1) % 4),
                    self.start_T + (self.size_square + self.size_line) * ((i + 1) // 4),
                )
                del self.tiles[i]
                var = True
        for i in range(16):
            if i in self.tiles and i + 1 not in self.tiles and (i + 1) % 4 != 0:
                self.tiles[i + 1] = Tile(
                    i + 1,
                    self.size_square,
                    self.tiles[i].value,
                    self.start_L + (self.size_square + self.size_line) * ((i + 1) % 4),
                    self.start_T + (self.size_square + self.size_line) * ((i + 1) // 4),
                )
                del self.tiles[i]
                var = True
        for i in range(16):
            if i in self.tiles and i + 1 not in self.tiles and (i + 1) % 4 != 0:
                self.tiles[i + 1] = Tile(
                    i + 1,
                    self.size_square,
                    self.tiles[i].value,
                    self.start_L + (self.size_square + self.size_line) * ((i + 1) % 4),
                    self.start_T + (self.size_square + self.size_line) * ((i + 1) // 4),
                )
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
                self.tiles[i - 1] = Tile(
                    i - 1,
                    self.size_square,
                    self.tiles[i].value,
                    self.start_L + (self.size_square + self.size_line) * ((i - 1) % 4),
                    self.start_T + (self.size_square + self.size_line) * ((i - 1) // 4),
                )
                del self.tiles[i]
                var = True

        for i in range(15, -1, -1):
            if i in self.tiles and i - 1 not in self.tiles and i % 4 != 0:
                self.tiles[i - 1] = Tile(
                    i - 1,
                    self.size_square,
                    self.tiles[i].value,
                    self.start_L + (self.size_square + self.size_line) * ((i - 1) % 4),
                    self.start_T + (self.size_square + self.size_line) * ((i - 1) // 4),
                )
                del self.tiles[i]
                var = True

        for i in range(15, -1, -1):
            if i in self.tiles and i - 1 not in self.tiles and i % 4 != 0:
                self.tiles[i - 1] = Tile(
                    i - 1,
                    self.size_square,
                    self.tiles[i].value,
                    self.start_L + (self.size_square + self.size_line) * ((i - 1) % 4),
                    self.start_T + (self.size_square + self.size_line) * ((i - 1) // 4),
                )
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
                self.tiles[i + 4] = Tile(
                    i + 4,
                    self.size_square,
                    self.tiles[i].value,
                    self.start_L + (self.size_square + self.size_line) * ((i + 4) % 4),
                    self.start_T + (self.size_square + self.size_line) * ((i + 4) // 4),
                )
                del self.tiles[i]
                var = True

        for i in range(12):
            if i in self.tiles and i + 4 not in self.tiles:
                self.tiles[i + 4] = Tile(
                    i + 4,
                    self.size_square,
                    self.tiles[i].value,
                    self.start_L + (self.size_square + self.size_line) * ((i + 4) % 4),
                    self.start_T + (self.size_square + self.size_line) * ((i + 4) // 4),
                )
                del self.tiles[i]
                var = True

        for i in range(12):
            if i in self.tiles and i + 4 not in self.tiles:
                self.tiles[i + 4] = Tile(
                    i + 4,
                    self.size_square,
                    self.tiles[i].value,
                    self.start_L + (self.size_square + self.size_line) * ((i + 4) % 4),
                    self.start_T + (self.size_square + self.size_line) * ((i + 4) // 4),
                )
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
        val2 = random.choices((2, 4), [5, 1])[0]
        self.tiles[num1] = Tile(
            num1,
            self.size_square,
            2,
            self.start_L + (self.size_square + self.size_line) * (num1 % 4),
            self.start_T + (self.size_square + self.size_line) * (num1 // 4),
        )
        self.tiles[num2] = Tile(
            num2,
            self.size_square,
            val2,
            self.start_L + (self.size_square + self.size_line) * (num2 % 4),
            self.start_T + (self.size_square + self.size_line) * (num2 // 4),
        )

    def get_board_state(self):
        state = [0] * 16
        for i in range(16):
            if i in self.tiles:
                state[i] = self.tiles[i].value
        return state

    def wait(self):
        self.draw()
        pygame.display.flip()
        pygame.time.wait(500)
        

    def move(self, a):
        # 0 - > left, 1 up, 2 down 3 right
        res = False
        if a == 0:
            res = self.moveleft()
            

        elif a == 1:
            res = self.moveup()
            

        elif a == 2:
            res = self.movedown()
            

        elif a == 3:
            res = self.moveright()
            

        if res:
            avail = [i for i in range(16) if i not in self.tiles]
            num1 = random.choice(avail)
            self.tiles[num1] = Tile(
            num1,
            self.size_square,
            random.choices((2, 4), [9, 1])[0],
            self.start_L + (self.size_square + self.size_line) * (num1 % 4),
            self.start_T + (self.size_square + self.size_line) * (num1 // 4),
            )

    def lose(self):
        avail = [i for i in range(16) if i not in self.tiles]

        # length check
        if len(avail) != 0:
            return False

        # lose check
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

    def step(self, action):
        self.move(action)
        # pygame.display.flip()
