#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Elliott Kim
# author: Elliott Kim
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

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

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1
        
        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(0, 3):
            for c in range(0, 3):
                self.tiles[r][c] = int(digitstr[3 * r + c])
                if(self.tiles[r][c] == 0):
                    self.blank_r = r
                    self.blank_c = c

    ### Add your other method definitions below. ###

    def __repr__(self):
        """constructs, each numeric tile should be represented by the 
        appropriate single-character string, followed by a single space
        """
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles)):
                if self.tiles[r][c] == 0:
                    s += '_'
                    s += ' '
                else:
                    s += str(self.tiles[r][c])
                    s += ' '
            s += '\n'
        
        return s
    
    def move_blank(self, direction):
        """takes as input a string direction that specifies the direction in 
        which the blank should move, and that attempts to modify the contents 
        of the called Board object accordingly.
        """
        c = self.blank_c
        r = self.blank_r
        
        if direction == 'up':
            r = self.blank_r - 1
        
        elif direction == 'down':
            r = self.blank_r + 1
        
        elif direction == 'left':
            c = self.blank_c - 1
        
        elif direction == 'right':
            c = self.blank_c + 1
        
        else:
            print("unknown direction:", direction)
            return False
        
        if r >= 3 or c >= 3 or r < 0 or c < 0:
            return False
        
        else:
            x = self.tiles[r][c]
            self.tiles[r][c] = 0
            self.tiles[self.blank_r][self.blank_c] = x
            self.blank_c = c
            self.blank_r = r
            return True
        
    def digit_string(self):
        """that creates and returns a string of digits that corresponds to the 
        current contents of the called Board object’s tiles attribute.
        """
        s = ''
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[row])):
                s += str(self.tiles[row][col])
        return s
    
    def copy(self):
        """that returns a newly-constructed Board object that is a deep copy 
        of the called object 
        """
        new = Board(self.digit_string())
        return new
    
    def num_misplaced(self):
        """that counts and returns the number of tiles in the called Board 
        object that are not where they should be in the goal state.
        """
        count = 0
        d = self.digit_string()
        final = '012345678'
        
        for num in range(9):
            if d[num] == '0' or d[num] == final[num]:
                count += 0
            else:
                count += 1
        
        return count
    
    def __eq__(self, other):
        """that overloads the == operator – creating a version of the operator 
        that works for Board objects
        """
        if self.digit_string() == other.digit_string():
            return True
        
        else:
            return False
        
    def new_function(self):
        """ returns a value int of how far the numbers are apart from each other
        """
        goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        prior = 0
        for row in range(len(self.tiles)):#row
            for col in range(len(self.tiles[0])):#column
                tiles = self.tiles[row][col]
                if tiles != goal[row][col]:
                    prior += abs(row - tiles // 3)
                    prior += abs(col - tiles % 3)

        return prior