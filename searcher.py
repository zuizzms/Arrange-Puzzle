#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Zuizz Saeed
# email: zuizzms@bu.edu
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
        """
        constructs a new Searcher object by initializing:
        - states for the Searcher‘s list of untested states (empty list)
        - num_tested will keep track of how many states the Searcher tests (0)
        - depth_limit that specifies how deep in the state-space search tree 
          the Searcher will go
        """
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit
        
    def add_state(self, new_state):
        """
        takes a single State object called new_state and adds it to the Searcher‘s
        list of untested states
        """
        self.states += [new_state]
        
    def should_add(self, state):
        """
        takes a State object called state and returns True if the called Searcher
        should add state to its list of untested states, and False otherwise
        """
        if self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        elif state.creates_cycle():
            return False
        return True
    
    def add_states(self, new_states):
        """
        takes a list State objects called new_states, and that processes the
        elements of new_states one at a time 
        """
        for s in new_states:
            if self.should_add(s) == True:
                self.add_state(s)
                
    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self, init_state):
        """
        performs a full state-space search that begins at the specified initial
        state init_state and ends when the goal state is found or when the 
        Searcher runs out of untested states.
        """
        self.add_state(init_state)
        while len(self.states) > 0:
            s = self.next_state()
            self.num_tested += 1
            if s.is_goal():
                return s
            else:
                self.add_states(s.generate_successors())
        return None

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


### Add your BFSeacher and DFSearcher class definitions below. ###
class BFSearcher(Searcher):
    """ A Class for searcher objects that perform breadth-first search (BFS) 
    instead of random search. BFS involves always choosing one the untested
    states that has the smallest depth (i.e., the smallest number of moves
    from the initial state)
    """
    def next_state(self):
        """
        Rather than choosing at random from the list of untested states, this 
        version of next_state should follow FIFO (first-in first-out) ordering 
        – choosing the state that has been in the list the longest.
        """
        s = self.states[0]
        self.states.remove(s)
        return s
    
class DFSearcher(Searcher):
    """
    A class for searcher objects that perform depth-first search (DFS) instead
    of random search. DFS involves always choosing one the untested states that 
    has the largest depth (i.e., the largest number of moves from the initial 
    state)
    """
    def next_state(self):
        """
        Rather than choosing at random from the list of untested states, this 
        version of next_state should follow LIFO (last-in first-out) ordering 
        – choosing the state that was most recently added to the list.
        """
        s = self.states[-1]
        self.states.remove(s)
        return s 

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###
def h1(state):
    """
    computes and returns an estimate of how many additional moves are needed
    to get from state to the goal state 
    """
    return state.board.num_misplaced()

def h2(state):
    """
    computes total of incorrect rows and columns for misplaced tiles
    """
    return state.board.incRows() + state.board.incCols()

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    def __init__(self, heuristic):
        """ constructs a new GreedySearcher object
        - does not use depth limit (-1)
        - attribute heuristic stores reference to heuristic function
        """
        super().__init__(-1)
        self.heuristic = heuristic
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)
    
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
    
    def add_state(self, state):
        """
        Rather than simply adding the specified state to the list of untested
        states, the method should add a sublist that is a [priority, state] pair,
        where priority is the priority of state that is determined by calling the 
        priority method.
        """
        self.states += [[self.priority(state), state]]
        
    def next_state(self):
        """
        This version of next_state should choose one of the states with the 
        highest priority.
        """
        highest = max(self.states)
        highestState = highest[-1]
        self.states.remove(highest)
        return highestState

### Add your AStarSeacher class definition below. ###
class AStarSearcher(GreedySearcher):
    """
    class for informed search algorithm that assigns a priority to each state
    based on a heuristic function, and that selects the next state based on those
    priorities. Takes into account the cost that has already been expended to get 
    to that state
    """
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * (self.heuristic(state) + state.num_moves)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

