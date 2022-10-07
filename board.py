#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Zuizz Saeed
# email: zuizzms@bu.edu
#
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        count = 0
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                self.tiles[i][j] = digitstr[count]
                count += 1
                if self.tiles[i][j] == '0':
                    self.blank_r = i
                    self.blank_c = j

    ### Add your other method definitions below. ###
    def __repr__(self):
        """
        returns a string representation of a Board object with hyphen as blank space
        """
        result = ''
        count = 0
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                if self.tiles[i][j] == '0':
                    result += '_ '
                else:
                    result += self.tiles[i][j] + ' '
                count += 1
                if count % 3 == 0:
                    result += '\n'
        return result
    
    def move_blank(self, direction):
        """
        takes as input a string direction that specifies the direction in which
        the blank should move, and attempts to modify the contents of the
        called Board object accordingly
        """
        if direction not in 'leftrightupdown':
            return False
        newRow = self.blank_r
        newCol = self.blank_c
        if direction == 'down':
            newRow = self.blank_r + 1
        elif direction == 'up':
            newRow = self.blank_r - 1
        elif direction == 'left':
            newCol = self.blank_c - 1
        elif direction == 'right':
            newCol = self.blank_c + 1
        
        if 0 > newRow or newRow > 2 or 0 > newCol or newCol > 2:
            return False
        
        if direction == 'down':
            self.tiles[self.blank_r][self.blank_c] = \
                self.tiles[self.blank_r + 1][self.blank_c]
            self.tiles[self.blank_r+1][self.blank_c] = '0'
            self.blank_r += 1
        elif direction == 'up':
            self.tiles[self.blank_r][self.blank_c] = \
                self.tiles[self.blank_r - 1][self.blank_c]
            self.tiles[self.blank_r -1][self.blank_c] = '0'
            self.blank_r -= 1
        elif direction == 'left':
            self.tiles[self.blank_r][self.blank_c] = \
                self.tiles[self.blank_r][self.blank_c - 1]
            self.tiles[self.blank_r][self.blank_c - 1] = '0'
            self.blank_c -= 1
        elif direction == 'right': 
            self.tiles[self.blank_r][self.blank_c] = \
                self.tiles[self.blank_r][self.blank_c + 1]
            self.tiles[self.blank_r][self.blank_c + 1] = '0'
            self.blank_c += 1
        return True
    
    def digit_string(self):
        """
        creates and returns a string of digits that corresponds to the current
        contents of the called Board object’s tiles attribute
        """
        result = ''
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                result += self.tiles[i][j]
        return result
    
    def copy(self):
        """
        returns a newly-constructed Board object that is a deep copy of the
        called object
        """
        new = Board(self.digit_string())
        return new
    
    def num_misplaced(self):
        """
        counts and returns the number of tiles in the called Board object that
        are not where they should be in the goal state
        """
        count = 0
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                if self.tiles[i][j] != GOAL_TILES[i][j] and self.tiles[i][j] != '0':
                    count+=1
        return count
    
    def __eq__(self, other):
        """
        called when the == operator is used to compare two Board objects. 
        The method should return True if the called object (self) and the 
        argument (other) have the same values for the tiles attribute, and 
        False otherwise
        """
        if self.tiles == other.tiles:
            return True
        else:
            return False
    def incRows(self):
        """
        Adds 1 for every time a misplaced tile is in the wrong row 
        """
        count = 0
        string = self.digit_string()
        if '1' not in string[0:3]:    # row 1 corresponds to string[0:3]
            count += 1
        if '2' not in string[0:3]:
            count += 1
        if '3' not in string[3:6]:
            count += 1
        if '4' not in string[3:6]:
            count += 1
        if '5' not in string[3:6]:
            count += 1
        if '6' not in string[6:9]:
            count += 1
        if '7' not in string[6:9]:
            count += 1
        if '8' not in string[6:9]:
            count += 1
        return count
    def incCols(self):
        """
        Adds 1 for every time a misplaced tile is in the wrong column
        """
        count = 0
        string = self.digit_string()
        if '1' != string[1] and '1' != string[4] and '1' != string[7]:
            count += 1
        if '2' != string[2] and '2' != string[5] and '2' != string[8]:
            count += 1
        if '3' != string[0] and '3' != string[3] and '3' != string[6]:
            count += 1
        if '4' != string[1] and '4' != string[4] and '4' != string[7]:
            count += 1
        if '5' != string[2] and '5' != string[5] and '5' != string[8]:
            count += 1
        if '6' != string[0] and '6' != string[3] and '6' != string[6]:
            count += 1
        if '7' != string[1] and '7' != string[4] and '7' != string[7]:
            count += 1
        if '8' != string[2] and '8' != string[5] and '8' != string[8]:
            count += 1
        return count
                
                
        
    
    
    
            
        
        
                    
        























