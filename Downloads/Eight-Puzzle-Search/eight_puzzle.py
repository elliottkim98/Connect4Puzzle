#
# eight_puzzle.py (Final Project)
#
# driver/test code for state-space search on Eight Puzzles
#
# name: Elliott Kim
# author: Elliott Kim
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

from searcher import *
from timer import *

def create_searcher(algorithm, depth_limit = -1, heuristic = None):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * depth_limit - an optional parameter that can be used to
            specify a depth limit 
          * heuristic - an optional parameter that can be used to pass
            in a heuristic function
            
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(depth_limit)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(depth_limit)
    elif algorithm == 'DFS':
        searcher = DFSearcher(depth_limit)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(depth_limit, heuristic)
    elif algorithm == 'A*':
        searcher = AStarSearcher(depth_limit, heuristic)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, depth_limit = -1, heuristic = None):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * depth_limit - an optional parameter that can be used to
            specify a depth limit 
          * heuristic - an optional parameter that can be used to pass
            in a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')

    searcher = create_searcher(algorithm, depth_limit, heuristic)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()

def process_file(filename, algorithm, depth_limit = -1, heuristic = None):
    """opens the file with the specified filename for reading, and it should 
    use a loop to process the file one line at a time.
    perform the cumulative computations needed to report the following 
    summary statistics after processing the entire file:
    -number of puzzles solved
    -average number of moves in the solutions
    -average number of states tested
    """
    f = open(filename,'r')
    puzzles = 0 
    tested = 0
    moves = 0
    
    for line in f:
        string = str(line[0:9])
        board = Board(string)
        algorithm = str(algorithm)
        s = State(board, None, 'init')
        searcher = create_searcher(algorithm, depth_limit, heuristic)
        soln = None
        
        try:
            soln = searcher.find_solution(s)
            
            if soln == None:
                print(string + ': no solution')
            
            else:
                print(string + ':', soln.num_moves,'moves,',searcher.num_tested, 'states tested')
                puzzles += 1
                moves += soln.num_moves
                tested += searcher.num_tested

        except KeyboardInterrupt:
            print(string + ':' + ' search terminated, no solution')
            soln = None
    
    if puzzles != 0:
        print()
        print('solved',puzzles,'puzzles')
        print('averages:', moves/puzzles,'moves,',tested/puzzles,'states tested')

    else:
        print('solved 0 puzzles')