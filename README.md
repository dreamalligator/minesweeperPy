![minesweeperPyLogo](https://stshrewsburydev.github.io/official_site/API/ProjectScreenshots/minesweeperPy/minesweeperPyLogo.png "minesweeperPy logo")

The minesweeperPy module for Python 3
=====================================

#### Made by Steven Shrewsbury Dev. (AKA: stshrewsburyDev)


Screenshots:
------------

![RawTerminalUsage](https://stshrewsburydev.github.io/official_site/API/ProjectScreenshots/minesweeperPy/minesweeperPy0001.png "Raw terminal usage")

ChangeLogs:
-----------

Version 1.3 and 1.6

* Added ``BlankIdentifier`` to ``MineGen()`` so you can set custom blank cell identifiers
* Updated help information for the module

Version 1.4 and 1.5 had some major problems so the new version is 1.6

Installation:
-------------

###### Install with pip:

```
pip install minesweeperPy
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
columns = 12 # This will be the amount of columns in the grid (Must be 5+)
rows = 12 # This will be the amount of rows in the grid (Must be 5+)

MyNewGridGenerator = minesweeperPy.MineGen(columns, rows)
```

The number of cells in the grid is calculated by multiplying the column count by the row count:

| Columns | Rows | Cells |
|:-------:|:----:|:-----:|
| 10      | 10   | 100   |
| 25      | 20   | 500   |
| 48      | 50   | 2400  |

###### Generate a new grid:

```py
NumberOfMines = 25 # This will be the number of mines in the grid
#(Must be 1+ and not be more than the maximum space on the Grid generation
# (For example a 10x12 grid would have a maximum of 120 cells))

MyNewMinesweeperGrid = MyNewGridGenerator.GenerateGrid(NumberOfMines)
```

###### Output grid:

```py
>>>print(MyNewMinesweeperGrid)
{
  'grid': [['2', 'M', '1', '1', 'M'],
           ['M', '2', '1', '1', '1'],
           ['2', '2', ' ', ' ', ' '],
           ['M', '2', ' ', ' ', ' '],
           ['M', '2', ' ', ' ', ' ']
           ],
  'BlankIdentifier': ' '
}
 
>>>for row in MyNewMinesweeperGrid["grid"]:
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
>>>minesweeperPy.GridInfo(MyNewMinesweeperGrid)
{
  'GridColumns': 5,
  'GridRows': 5,
  'MineCount': 5,
  'NonMineCells': 20,
  'EmptyCells': 9, 
  'NumberedCells': 11
}

>>>
```

###### Generate a new grid generation with a custom blank identifer
```py
>>>columns = 12 # This will be the amount of columns in the grid (Must be 5+)
>>>rows = 12 # This will be the amount of rows in the grid (Must be 5+)
>>>customIdentifier = "/" # This will be the cell identifier in the grid (Must be a string value)
>>>NumberOfMines = 25 # This will be the number of mines in the grid

>>>MyNewGridGenerator = minesweeperPy.MineGen(columns, rows, customIdentifier)

>>>MyNewMinesweeperGrid = MyNewGridGenerator.GenerateGrid(NumberOfMines)

>>>print(MyNewMineSweeperGrid["grid"])
[['2', 'M', '1', '1', 'M'],
 ['M', '2', '1', '1', '1'],
 ['2', '2', '/', '/', '/'],
 ['M', '2', '/', '/', '/'],
 ['M', '2', '/', '/', '/']
 ]
```

###### Links:

* [GitHub repository page](https://github.com/stshrewsburyDev/minesweeperPy)
* [The module PyPi site](https://pypi.org/project/minesweeperPy/)
* [The stshrewsburyDev official site](https://stshrewsburydev.github.io/official_site/)
