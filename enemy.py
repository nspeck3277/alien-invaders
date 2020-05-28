import uuid

from random import randint
from random import choice


class EnemyPlane:
    def __init__(self, y_grid_size, time_elapsed, coordinates = None):
        color_choice = ["red", "blue"]
        if coordinates != None:
            self._x_pos = coordinates[0]
            self._y_pos = coordinates[1]
            self._speed = time_elapsed**(1/3)
            self._color = choice(color_choice)
        else:
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
        spawn_coordinates = [[1920, 220], [1920, 328], [1920, 436], [1920, 544], [1920, 652], [1920, 760], [1920, 868],[1920, 976]]
        enemy_planes = []
        for x in range(5):
            random_coordinate = spawn_coordinates[randint(0, len(spawn_coordinates)-1)]
            enemy_planes.append(EnemyPlane(y_grid_size, time_elapsed, coordinates = random_coordinate))
            spawn_coordinates.remove(random_coordinate)
        return enemy_planes
        