'''
DEFINE SCREEN PARAMETERS
'''

class Matrix(object):
    def __init__(self, rows, columns, default_character= "@"):
        self.rows = rows
        self.columns = columns
        # Define 2D LIST
        #eg if rows = 2 and columns = 4
        #[['@', '@', '@', '@'], ['@', '@', '@', '@']]
        #Using a For Loop on this result , We have
        #['@', '@', '@', '@'], we can see that we have 2 rows and 4 columns of '@'
        #['@', '@', '@', '@']
        self.grid = [[default_character] * self.columns for _ in range(self.rows)]



    def display_matrix(self):
        '''
        
        :return: display a string of concat List
        '''

        for row in self.grid:
            print("".join(row))




    def update_character_in_matrix(self, row_number, columns_number, newchar):
        #Check the Limite of the  Board
        if 0 <= row_number < self.rows:
            if 0 <= columns_number < self.columns:
                self.grid[row_number][columns_number] = newchar
                return

        raise IndexError("Your Char are  Out of Bound")






