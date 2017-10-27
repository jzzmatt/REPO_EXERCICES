from direction import Direction
'''
DEFINE CHARACTER ATTRIBUTE
'''
class Player(object):
    def __init__(self, symbol, startx=0, starty=0, velx=1, vely=1, trace='*'):
        self.symbol = symbol

        self.x = startx
        self.y = starty

        self.velx = velx
        self.vely = vely
        self.trace = trace




    def move(self, direction):
        '''
        
        :param direction: Move the Player relativly to the Direction
        :return: New Player Coordonate
        '''
        pl_direction = Direction()


        #IF Y
        if direction == pl_direction.Down:
            self.y += self.vely


        elif direction == pl_direction.Up:
            self.y -= self.vely

        #IF X
        elif direction == pl_direction.Left:
            self.x -= self.velx


        elif direction == pl_direction.Rigth:
            self.x += self.velx


