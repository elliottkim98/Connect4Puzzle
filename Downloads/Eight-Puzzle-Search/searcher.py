#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Elliott Kim
# author: Elliott Kim
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    
    def __init__(self, depth_limit):
        """new Searcher object, attribute states for the Searcher‘s list of untested states
        num_tested that will keep track of how many states the Searcher tests
        depth_limit that specifies how deep in the state-space search tree the 
        Searcher will go
        """
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit
        
    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s

    def should_add(self, state):
        """takes a State object called state and returns True if the called 
        Searcher should add state to its list of untested states, and False otherwise.
        """
        if self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        
        elif state.creates_cycle() == True:
            return False
        
        else:
            return True
        
    def add_state(self, new_state):
        """that adds takes a single State object called new_state and adds it 
        to the Searcher‘s list of untested states
        """
        self.states += [new_state]
        
    def add_states(self, new_states):
        """ that takes a list State objects called new_states, and that processes 
        the elements of new_states one at a time
        """
        for s in new_states:
            if self.should_add(s):
                self.add_state(s)
                
    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self, init_state):
        """that performs a full random state-space search, stopping when the 
        goal state is found or when the Searcher runs out of untested states.
        """
        self.add_state(init_state)
        
        while len(self.states) > 0:
            self.num_tested += 1
            s = self.next_state()
            if s.is_goal() == True:
                return s
            
            else:
                self.add_states(s.generate_successors())
                
        return None
### Add your BFSeacher and DFSearcher class definitions below. ###

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

class BFSearcher(Searcher):
    """that perform breadth-first search (BFS) instead of random search
    """
    def next_state(self):
        """follow FIFO (first-in first-out) ordering – choosing the state 
        that has been in the list the longest
        """
        s = self.states[0]
        self.states.remove(s)
        return s

class DFSearcher(Searcher):
    """DFS involves always choosing one the untested states that has the 
    largest depth (i.e., the largest number of moves from the initial state).
    """
    def next_state(self):
        """follow LIFO (last-in first-out) ordering – choosing the state 
        that was most recently added to the list.
        """
        s = self.states[-1]
        self.states.remove(s)
        return s

### Add your other heuristic functions here. ###
def h1(state):
    """a heuristic function that returns number of misplaced boards
    """
    return state.board.num_misplaced()

def h2(state):
    """a heuristic function that returns how an integer of how tiles are 
    far from goal board
    """
    return int(state.board.new_function())


class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    
    def priority(self, state):
        """computes and returns the priority of that state
        """
        prior = -1 * self.heuristic(state)
        return prior

    def add_state(self, state):
        """add a sublist that is a [priority, state] pair, where priority 
        is the priority of state, as determined by calling the priority method.
        """
        p = self.priority(state)
        self.states += [[p, state]]

    def next_state(self):
        """next_state should choose one of the states with the highest priority.
        """
        s = max(self.states)
        self.states.remove(s)
        return s[1]

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s

    def __init__(self, depth_limit, heuristic):
        """ constructor for a GreedySearcher object
        inputs:
         * depth_limit - the depth limit of the searcher
         * heuristic - a reference to the function that should be used 
         when computing the priority of a state
         """
    # add code that calls the superclass constructor
        super().__init__(-1)
        self.heuristic = heuristic

### Add your AStarSeacher class definition below. ###

class AStarSearcher(GreedySearcher):
    """A* is an informed search algorithm that assigns a priority to each state 
    based on a heuristic function, and that selects the next state based 
    on those priorities.
    """
    def priority(self, state):
        """heuristic is the value that the selected heuristic function assigns 
        to the state, and num_moves is the number of moves that it took to get 
        to that state from the initial state.
        """
        prior = -1 * (self.heuristic(state) + state.num_moves)
        return prior