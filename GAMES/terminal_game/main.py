from matrix import Matrix
from character import Player
from direction import Direction


#define the dimension of the Terminal
rows, column =  23, 40

matrix = Matrix(rows,column, default_character='')
player = Player("&")
direction = Direction()

class Menu(object):
    def __init__(self):
        self.display = '''
        ----* TERMINAL GAME *----
                Press:
        'U'  For Move Your Player Up
        'D'  For Move Your Player Down
        'L'  For Move Your Player Left
        'R'  For Move Your Player Right
        'Q'  For Quitting
        '''
    @property
    def choice(self):
        choice_dict = {
            "U": direction.Up,
            "D": direction.Down,
            "L": direction.Left,
            "R": direction.Rigth
        }
        return choice_dict




menu = Menu()
print(menu.display)

matrix.update_character_in_matrix(player.y, player.x,player.symbol)

while True:
    matrix.display_matrix()

    matrix.update_character_in_matrix(player.y, player.x, player.trace)


    player_direction = input("Enter Your Direction: ").upper()

    if player_direction == "Q" :
        print("Quitting....")
        break

    elif player_direction not in menu.choice:
        print("Refer to the Menu Option !!!")

    else: #Based on the Position, should Update the Player Position on Grid
        get_move = menu.choice.get(player_direction)
        player.move(get_move)

    matrix.update_character_in_matrix(player.y, player.x, player.symbol)


