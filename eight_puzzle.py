#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: Zuizz Saeed
# email: zuizzms@bu.edu
#

from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
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
def process_file(filename, algorithm, param):
    """
    Opens file for reading, taking 3 inputs:
    - string filename specifying the name of a text file in which each line is 
    a digit string for an eight puzzle
    - string algorithm that specifies which state-space search algorithm should
    be used to solve the puzzles
    - third input param that allows you to specify a parameter for the searcher
     either a depth limit (for the uninformed search algorithms) or a choice of 
     heuristic function (for the informed search algorithms)
    """
    f = open(filename, 'r')
    numSolved = 0
    sumMoves = 0
    sumStates = 0
    for line in f:
        line = line[:-1]
        init_board = Board(line)
        init_state = State(init_board, None, 'init')
        searcher = create_searcher(algorithm, param)
        soln = None
        try:
            soln = searcher.find_solution(init_state)
            if soln == None:
                print(line + ':', 'no solution')
            else: 
                print(line + ':', soln.num_moves, 'moves,', searcher.num_tested,\
                      'states tested')
                numSolved += 1
                sumMoves += soln.num_moves
                sumStates += searcher.num_tested
        except KeyboardInterrupt:
            print(line + ':', 'search terminated, no solution')
            soln = None
    if numSolved == 0:
        print()
        print('solved: 0 puzzles')
    else:
        avgMoves = sumMoves/numSolved
        avgStates = sumStates/numSolved
        print()
        print('solved', numSolved, 'puzzles')
        print('averages:', avgMoves, 'moves,', avgStates, 'states tested')
        
        
        
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
