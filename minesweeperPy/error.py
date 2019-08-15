"""
minesweeperPy.error
The minesweeper generator in Python 3
Made by Steven Shrewsbury. (stshrewsburyDev)
"""

class InvalidGridSize(Exception):
    """This is triggered when a invalid size is entered for a grid"""
    pass

class InvalidCellIdentifier(Exception):
    """This is triggered when a invalid cell identifier is parsed in"""
    pass

class InvalidMineCount(Exception):
    """This is triggered when a invalid mine count is parsed in"""
    pass

class InvalidLevel(Exception):
    """This is triggered when a invalid level is parsed in"""
    pass
