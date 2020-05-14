import uuid

from random import randint
from random import choice


class EnemyPlane:
    def __init__(self, y_grid_size, time_elapsed):
        color_choice = ["red", "blue"]
        enemy_planes = [[ 1920, randint(1, 8) * y_grid_size+4, time_elapsed**(1/3)] for _ in range(5) ] 
        self._id = uuid.uuid4().hex
        self._x_pos = enemy_planes[randint(0,len(enemy_planes) - 1)][0]
        self._y_pos = enemy_planes[randint(0,len(enemy_planes) - 1)][1]
        self._speed = enemy_planes[randint(0,len(enemy_planes) - 1)][2]
        self._color = choice(color_choice)
    
    @property
    def id(self):
        return self._id
    
    @property
    def x_pos(self):
        return self._x_pos
    
    @property
    def y_pos(self):
        return self._y_pos
    
    @property
    def speed(self):
        return self._speed
    @property
    def color(self):
        return self._color
    
    def enemy_movement(self):
        self._x_pos -= x_grid_size/self._speed
    
    def create_planes(y_grid_size, time_elapsed):
        return [ EnemyPlane(y_grid_size, time_elapsed) for _ in range(6) ]
        