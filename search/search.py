# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state
        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state
        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take
        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """

    print "------------------------------------------------------------------------------"
    print
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    print

    fringe = util.Stack()  # my fringe
    coord = []
    path = []  # keeps track of the path
    discovered = set()  # keeps track of what is visited
    finalPath = []
    # set the start state
    fringe.push((problem.getStartState(), ''))  # add the start state to the fringe
    # path stuff
    while not fringe.isEmpty():
        # pop the first value from the fringe
        currState = fringe.pop()
        print "currrState", currState  # THIS IS FOR DEBUGGING
        # after popping add the the location of the one that was popped

        # check to see if it is a goal state and if it is return the path array
        if problem.isGoalState(currState[0]):
            directions = currState[1].split(".")  # split using '.' as a delimiter
            del directions[-1]  # there is an extra element which is blank so delete it
            for direction in reversed(directions):  # reverse to get the pathing
                finalPath.append(direction)  # add each element to the final pathing
            return finalPath  # RETURN TO THE FINAL PATH AND WIN!!!!!!!!!!!!
        # this state has now been added
        discovered.add(currState[0])
        # get the successors of the current state as visited
        successors = problem.getSuccessors(currState[0])
        # if they are not already added then add them to the stack
        for successor in successors:
            if successor[0] not in discovered:
                # add to the fringe
                fringe.push(
                    (successor[0], successor[1] + '.' + currState[1]))  # copy the parent path and append the successor


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    print "------------------------------------------------------------------------------"
    print
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    print

    fringe = util.Queue()  # my fringe
    coord = []
    path = []  # keeps track of the path
    discovered = set()  # keeps track of what is visited
    finalPath = []
    # set the start state
    fringe.push((problem.getStartState(), ''))  # add the start state to the fringe
    # path stuff
    while not fringe.isEmpty():
        # pop the first value from the fringe
        currState = fringe.pop()
        if currState[0] not in discovered:
            discovered.add(currState[0])
            successors = problem.getSuccessors(currState[0])
            # if they are not already added then add them to the stack
            for successor in successors:
                ##if successor[0] not in discovered:
                # add to the fringe
                fringe.push(
                    (successor[0], successor[1] + '.' + currState[1]))  # copy the parent path and append the successor

        # print "currrState" ,currState THIS IS FOR DEBUGGING
        # after popping add the the location of the one that was popped
        # check to see if it is a goal state and if it is return the path array
        if problem.isGoalState(currState[0]):
            directions = currState[1].split(".")  # split using '.' as a delimiter
            del directions[-1]  # there is an extra element which is blank so delete it
            for direction in reversed(directions):  # reverse to get the pathing
                finalPath.append(direction)  # add each element to the final pathing
            return finalPath  # RETURN TO THE FINAL PATH AND WIN!!!!!!!!!!!!
            # this state has now been added

            # get the successors of the current state as visited

    print "Dr. Dan DEBUG - If your code makes it here, then we left the while loop w/o finding solution"
    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    print "------------------------------------------------------------------------------"
    print
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    print

    fringe = util.PriorityQueue()  # my fringe
    coord = []
    path = []  # keeps track of the path
    discovered = set()  # keeps track of what is visited
    finalPath = []
    # set the start state
    fringe.push((problem.getStartState(), ''), 0)  # add the start state to the fringe
    # path stuff
    while not fringe.isEmpty():
        # pop the first value from the fringe
        currState = fringe.pop()
        # print "currrState" ,currState THIS IS FOR DEBUGGING
        # after popping add the the location of the one that was popped

        # check to see if it is a goal state and if it is return the path array
        if problem.isGoalState(currState[0]):
            directions = currState[1].split(".")  # split using '.' as a delimiter
            del directions[-1]  # there is an extra element which is blank so delete it
            for direction in reversed(directions):  # reverse to get the pathing
                finalPath.append(direction)  # add each element to the final pathing
            return finalPath  # RETURN TO THE FINAL PATH AND WIN!!!!!!!!!!!!
        # this state has now been added
        discovered.add(currState[0])
        # get the successors of the current state as visited
        successors = problem.getSuccessors(currState[0])
        # if they are not already added then add them to the stack
        for successor in successors:
            if successor[0] not in discovered:
                # add to the fringe
                tempPath = []
                directions = currState[1].split(".")  # split using '.' as a delimiter
                del directions[-1]  # there is an extra element which is blank so delete it
                for direction in reversed(directions):  # reverse to get the pathing
                    tempPath.append(direction)  # add each element to the final pathing
                fringe.push((successor[0], successor[1] + '.' + currState[1]),
                            problem.getCostOfActions(tempPath))  # copy the parent path and append the successor


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    print "------------------------------------------------------------------------------"
    print
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    print

    fringe = util.PriorityQueue()  # my fringe
    coord = []
    path = []  # keeps track of the path
    discovered = set()  # keeps track of what is visited
    finalPath = []
    # set the start state
    fringe.push((problem.getStartState(), ''), 0)  # add the start state to the fringe
    # path stuff
    while not fringe.isEmpty():
        # pop the first value from the fringe
        currState = fringe.pop()
        # after popping add the the location of the one that was popped
        if currState[0] not in discovered:
            discovered.add(currState[0])
            successors = problem.getSuccessors(currState[0])
            for successor in successors:

                # add to the fringe
                tempPath = []
                directions = currState[1].split(".")  # split using '.' as a delimiter
                del directions[-1]  # there is an extra element which is blank so delete it
                for direction in reversed(directions):  # reverse to get the pathing
                    tempPath.append(direction)  # add each element to the final pathing
                hCost = heuristic(currState[0], problem)
                fringe.push((successor[0], successor[1] + '.' + currState[1]),
                            len(tempPath) + hCost)  # copy the parent path and append the successor

        # check to see if it is a goal state and if it is return the path array
        if problem.isGoalState(currState[0]):
            directions = currState[1].split(".")  # split using '.' as a delimiter
            del directions[-1]  # there is an extra element which is blank so delete it
            for direction in reversed(directions):  # reverse to get the pathing
                finalPath.append(direction)  # add each element to the final pathing
            return finalPath  # RETURN TO THE FINAL PATH AND WIN!!!!!!!!!!!!
            # this state has now been added

            # get the successors of the current state as visited

            # if they are not already added then add them to the stack


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

