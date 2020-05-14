import pygame
def draw_grid(window, x_grid_size, y_grid_size):    
    for x in range(0,1921,x_grid_size):
        vert_grid_start = (x, 0)
        vert_grid_end = (x,1080)
        pygame.gfxdraw.vline(window, x, 0, 1081, (255,255,255))
    
    for y in range(0,1081,y_grid_size):
        vert_grid_start = (0, y)
        vert_grid_end = (1920,y)
        pygame.gfxdraw.hline(window, 0, 1921, y, (255,255,255))

def get_rect(surface, entity):
    return surface.get_rect(center = (entity.x_pos, entity.y_pos))
    
