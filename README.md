![minesweeperPyLogo](https://stshrewsburydev.github.io/official_site/API/ProjectScreenshots/minesweeperPy/minesweeperPyLogo.png "minesweeperPy logo")

The minesweeperPy module for Python 3
=====================================

#### Made by Steven Shrewsbury Dev. (AKA: stshrewsburyDev)


Screenshots:
------------

![RawTerminalUsage](https://stshrewsburydev.github.io/official_site/API/ProjectScreenshots/minesweeperPy/minesweeperPy0002.png "Raw terminal usage")

ChangeLogs:
-----------

Version 1.8

* Error message names are now better to understand (uses custom Exceptions)
* minesweeperPy.error added

Installation:
-------------

###### Install with pip:

```
pip install minesweeperPy
```

###### Update with pip

```
pip install minesweeperPy --upgrade
```

###### Install from source:

```
python setup.py install
```

Using in your code:
-------------------

###### Import the module:

```py
import minesweeperPy
```

###### Make a new grid generation setting:

```py
columns = 5 # This will be the amount of columns in the grid (Must be 5+)
rows = 5 # This will be the amount of rows in the grid (Must be 5+)

myGridGen = minesweeperPy.mineGen(columns, rows)
```

The number of cells in the grid is calculated by multiplying the column count by the row count:

| Columns | Rows | Cells |
|:-------:|:----:|:-----:|
| 10      | 10   | 100   |
| 25      | 20   | 500   |
| 48      | 50   | 2400  |

###### Generate a new grid:

```py
numOfMines = 5 # This will be the number of mines in the grid
# Must be 0 or more
# Cannot be more than the total number of cells on the grid
#   eg: a 10x10 grid can have a max of 100 mines

myGrid = myGridGen.generateGrid(numOfMines)
```

###### Output grid:

```py
>>>print(myGrid)
{
  'grid': [['2', 'M', '1', '1', 'M'],
           ['M', '2', '1', '1', '1'],
           ['2', '2', ' ', ' ', ' '],
           ['M', '2', ' ', ' ', ' '],
           ['M', '2', ' ', ' ', ' ']
           ],
  'BlankIdentifier': ' ',
  'mineIdentifier': 'M'
}
 
>>>for row in myGrid["grid"]:
...    print(row)
...
['2', 'M', '1', '1', 'M']
['M', '2', '1', '1', '1']
['2', '2', ' ', ' ', ' ']
['M', '2', ' ', ' ', ' ']
['M', '2', ' ', ' ', ' ']

>>>
```

###### Get grid information:

```py
>>>minesweeperPy.gridInfo(grid=myGrid["grid"],
                          blankIdentifier=myGrid["blankIdentifier"],
                          mineIdentifier=myGrid["mineIdentifier"])
{
  'gridColumns': 5,
  'gridRows': 5,
  'mineCount': 5,
  'nonMineCells': 20,
  'emptyCells': 9,
  'numberedCells': 11,
  'NOTICE': 'If these results seem wrong re-run gridInfo() with the correct mine and blank cell identifiers'
}

>>>
```

###### Generate a new grid generation with a custom blank and mine identifiers
```py
>>>columns = 5 # This will be the amount of columns in the grid (Must be 5+)
>>>rows = 5 # This will be the amount of rows in the grid (Must be 5+)
>>>blankCustIdentifier = "/" # This will be the cell identifier for blank cells in the grid (Must be a string value and not a None type)
>>>mineCustIdentifier = "%" # This will be the cell identifier for mine cells in the grid (Must be a string value and not a None type)
>>>numOfMines = 5 # This will be the number of mines in the grid

>>>myGridGen = minesweeperPy.mineGen(columns, rows, blankCustIdentifier, mineCustIdentifier)

>>>myGrid = myGridGen.generateGrid(numOfMines)

>>>print(myGrid["grid"])
[['3', '%', '3', '1', '1'],
 ['%', '%', '4', '%', '1'],
 ['2', '3', '%', '2', '1'],
 ['/', '1', '1', '1', '/'],
 ['/', '/', '/', '/', '/']]
```

###### Generate a grid with a preset:
Without custom identifiers
```py
level = "easy" # This can be "easy", "medium", "hard" or "expert"
# This is not case sensitive so "eAsY" will still work

myGrid = minesweeperPy.preGenerate(level=level)
```

With custom identifiers
```py
level = "medium" # This can be "easy", "medium", "hard" or "expert"
blankCustIdentifier = "$" # This will be the identifier for blank cells
mineCustIdentifier = "!" # This will be the identifier for mines

myGrid = minesweeperPy.preGenerate(level=level,
                                   blankIdentifier=blankCustIdentifier,
                                   mineIdentifier=mineCustIdentifier)
```

###### Links:

* [GitHub repository page](https://github.com/stshrewsburyDev/minesweeperPy)
* [The module PyPi site](https://pypi.org/project/minesweeperPy/)
* [The stshrewsburyDev official site](https://stshrewsburydev.github.io/official_site/)
