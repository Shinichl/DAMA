import pygame

class Ficha: 
    def __init__(self, player):
        self.sprite = None
        self.position = None
        self.queen = False
        self.player = player
        if self.player == 1:
            self.sprite = pygame.image.load("./Imagenes/Ficha_Naranja.png")
        elif self.player == 2:
            self.sprite = pygame.image.load("./Imagenes/Ficha_Azul.png")
    
    def selected_piece(self):
        if self.player == 1:
            self.sprite = pygame.image.load("./Imagenes/Seleccion_Ficha_Naranja.png")
        elif self.player == 2:
            self.sprite = pygame.image.load("./Imagenes/Seleccion_de_ficha_Azul.png")
    
    def deselected_piece(self):
        if self.player == 1:
            self.sprite = pygame.image.load("./Imagenes/Ficha_Naranja.png")
        elif self.player == 2:
            self.sprite = pygame.image.load("./Imagenes/Ficha_Azul.png")

    def path_piece(self):
        if self.player == 1:
            path1 = (self.position[0] - 75, self.position[1] - 75)
            path2 = (self.position[0] + 75, self.position[1] - 75)
            return (path1, path2)
        elif self.player == 2:
            path1 = (self.position[0] + 75, self.position[1] + 75)
            path2 = (self.position[0] - 75, self.position[1] + 75)    
            return (path1, path2)
    
    def eathing_path(self, list_player1, list_player2):
        if self.player == 1:
            paths = self.path_piece()
            for other_player in list_player2:
                if paths[0] == other_player.position:
                    eat_path1 = (self.position[0] - 150, self.position[1] - 150)
                if paths[1] == other_player.position:
                    eat_path2 = (self.position[0] + 150, self.position[1] - 150)
            return (eat_path1, eat_path2)
        elif self.player == 2:
            paths = self.path_piece()
            for other_player in list_player1:
                if paths[0] == other_player.position:
                    eat_path1 = (self.position[0] + 150, self.position[1] + 150)
                elif paths[1] == other_player.position:
                    eat_path2 = (self.position[0] - 150, self.position[1] + 150)
            return (eat_path1, eat_path2)

    def move_piece(self, pos, available_moves, paths):
        if (pos[0], pos[1]) in available_moves and (pos[0], pos[1]) in paths:
            self.position = (pos[0], pos[1])
        else: 
            print("The new position is invalid")

    def eliminate(self):
        self.position = None

    

