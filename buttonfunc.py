from enums import CellState

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
