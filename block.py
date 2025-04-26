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

    def draw(self,screen):
        tiles=self.get_cell_position()
        for tile in tiles:
            tile_rect=pygame.Rect(tile.col*self.cell_size+1,tile.row*self.cell_size+1,self.cell_size-1,self.cell_size-1)
            pygame.draw.rect(screen,self.colors[self.id],tile_rect)
