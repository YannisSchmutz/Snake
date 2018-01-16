import pygame
from Settings import APPLE_IMG, BANANA_IMG, BLOCKSIZE
import random


class Food(pygame.sprite.Sprite):
    def __init__(self, food_type, pos_x, pos_y):
        super(Food, self).__init__()

        #self.image = pygame.Surface([width, height])
        #self.image.fill(color)
        food = {'apple': APPLE_IMG,
                'banana': BANANA_IMG}
        if food_type == 'random':
            randx = random.randrange(0, len(food.keys()))
            food_type = food.keys()[randx]

        self.img = pygame.image.load(food[food_type])

        #self.rect = self.image.get_rect()
        self._pos_x = pos_x
        self._pos_y = pos_y
        #self.rect[0] = pos_x
        #self.rect[1] = pos_y

    def draw(self, screen):
        screen.blit(self.img, (self._pos_x, self._pos_y))
        #pygame.draw.rect(screen, self._color, self.rect)

    def update_x_position(self, pos):
        self._pos_x = pos
        #self.rect[0] = pos

    def update_y_position(self, pos):
        #self.rect[1] = pos
        self._pos_y = pos

    def get_pos_x(self):
        #return self.rect[0]
        return self._pos_x

    def get_pos_y(self):
        #return self.rect[1]
        return self._pos_y

    def get_size(self):
        return BLOCKSIZE