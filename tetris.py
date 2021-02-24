import pygame

class Tetris:
    height = 0
    width = 0
    field = []
    score = 0
    state = "start"

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new.line)
# Initialize game engine
pygame.init()

size = (400, 500)
screen = pygame.display.set_mode((size))
pygame.display.set_caption("Tetris")


# Loop until user clicks the close button
done = False
fps = 25
clock = pygame.time.Clock()
counter = 0
clock.tick(fps)

game - Tetris(20, 10)
pressing_down = False

game = Tetris()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = TRUE
        if event.type == pygame.KEYDOWN: 
            if event.type == pygame.K_UP:
                game.rotate()
        if event.type == pygame.K_DOWN: 
            game.down()
        if event.type == pygame.K_LEFT: 
            game.left()
        if event.type == pygame.K_RIGHT: 
            game.right()
        if event.type == pygame.K_SPACE:
            game.go_space()
        if event.type == pygame.K_ESCAPE:
            game.__init__(20, 10)
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
            pressing_down = False
                   
# Adding Color
    WHITE = (255, 255, 255)
    screen.fill(WHITE)

pygame.quit()
    