The minesweeperPy module for Python 3
=====================================

#### Made by Steven Shrewsbury Dev. (AKA: stshrewsburyDev)


Screenshots:
------------

![RawTerminalUsage](https://stshrewsburydev.github.io/official_site/API/ProjectScreenshots/minesweeperPy/minesweeperPy0001.png "Raw terminal usage")

ChangeLogs:
-----------

* Patched error that was preventing the module from being imported on Linux based systems

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

MyNewGridGeneration = minesweeperPy.MineGen(columns, rows)
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

MyNewMinesweeperGrid = MyNewGridGeneration.GenerateGrid(NumberOfMines)
```

###### Output grid:

```py
>>>print(MyNewMinesweeperGrid)
[["M","1"," "," "," "],
 ["1","2","1","1"," "],
 [" ","1","M","2","1"],
 ["1","2","3","M","1"],
 ["1","M","2","1","1"]]
 
>>>for row in MyNewMinesweeperGrid:
...    print(row)
...
["M","1"," "," "," "]
["1","2","1","1"," "]
[" ","1","M","2","1"]
["1","2","3","M","1"]
["1","M","2","1","1"]

>>>
```

###### Links:

* [GitHub repository page](https://github.com/stshrewsburyDev/minesweeperPy)
* [The stshrewsburyDev official site](https://stshrewsburydev.github.io/official_site/)
