import uuid

class Laser:
    def __init__(self, position, color):
        
        self._id = uuid.uuid4().hex
        self._color = color
        
        if type(position) not in [tuple, list]:
            raise RuntimeError("failed to do")
        elif len(position) != 2:
            raise RuntimeError("failed to do")
        else:
            if not all(type(value) == int for value in position):
                raise RuntimeError("failed to do")
            else:
                self._x_pos, self._y_pos = position
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
    def color(self):
        return self._color
    
    def movement(self):
        self._x_pos += 35
        
    def remove_laser( id_number , lasers ):
        target = None 
    
        for each in lasers:
            if each.id == id_number:
                target = each
                break
        lasers.remove(target)
