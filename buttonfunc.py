from enums import *

#each function must return an enum
def placeholder():
    pass

def wallfunc():
    return CellState["WALL"]

def startfunc():
    return CellState["START"]

def endfunc():
    return CellState["END"]

def forestfunc():
    return CellState["FOREST"]

def breadthbutton():
    return CellState["BREADTH"]

def djbutton():
    return CellState["DJ_ALGO"]

def greedybutton():
    return CellState["GREEDY"]

def astarbutton():
    return CellState["ASTAR"]
