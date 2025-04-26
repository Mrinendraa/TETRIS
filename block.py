from colors import Colors
from position import Position
import pygame

class Block:
    def __init__(self,id):
        self.id = id
        self.cells={}
        self.cell_size=30
        self.row_offset=0
        self.col_offset=0
        self.rotation_state=0
        self.colors=Colors.get_cell_colors()


    def move(self,row,col):
        self.row_offset+=row
        self.col_offset+=col

    def get_cell_position(self):
        tiles=self.cells[self.rotation_state]
        moved_tiles=[]
        for position in tiles:
            position=Position(position.row+self.row_offset,position.col+self.col_offset)
            moved_tiles.append(position)
        return moved_tiles

    def rotate(self):
        self.rotation_state+=1
        if self.rotation_state==len(self.cells):
            self.rotation_state=0

    def undo_rotation(self):
        self.rotation_state-=1
        if self.rotation_state==0:
            self.rotation_state=len(self.cells)-1

    def draw(self,screen, x_offset=0, y_offset=0):
        tiles=self.get_cell_position()
        for tile in tiles:
            tile_rect=pygame.Rect(tile.col*self.cell_size+1 + x_offset, tile.row*self.cell_size+1 + y_offset, self.cell_size-1, self.cell_size-1)
            # Draw main block
            pygame.draw.rect(screen,self.colors[self.id],tile_rect)
            # Draw border outline
            pygame.draw.rect(screen,(255,255,255),tile_rect,2)
            # Draw shading effect (darker bottom and right edges)
            shade_color = (max(self.colors[self.id][0]-40,0), max(self.colors[self.id][1]-40,0), max(self.colors[self.id][2]-40,0))
            pygame.draw.line(screen, shade_color, (tile_rect.left, tile_rect.bottom-1), (tile_rect.right-1, tile_rect.bottom-1))  # bottom edge
            pygame.draw.line(screen, shade_color, (tile_rect.right-1, tile_rect.top), (tile_rect.right-1, tile_rect.bottom-1))  # right edge
