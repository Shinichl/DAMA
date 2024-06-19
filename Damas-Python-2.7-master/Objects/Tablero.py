import pygame

class Tablero:
    def __init__(self):
        self.board_image = pygame.image.load("./Imagenes/tablero_original.png")
        self.board = pygame.transform.scale(self.board_image, (600, 600))
        self.move_squares = []

    def movement_squares(self):
        xpos, ypos = 0, 525
        for row in range(8):
            for column in range(4):
                self.move_squares.append((xpos, ypos))
                xpos += 150
            if row % 2 == 0:
                xpos, ypos = 75, ypos - 75
            else:
                xpos, ypos = 0, ypos - 75

            

