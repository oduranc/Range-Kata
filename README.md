# Range-Kata

## Index
1. [Main file](./src/Range_oduranc/__init__.py)
2. [Unit Tests file](./src/Range_oduranc/example.py)
3. [How to Install](#how-to-install)
4. [Module Methods Examples](#module-methods-examples)

## How to Install

1. Check if you have the latest version of Python and pip installed in your computer.

2. If you haven't installed Python or is not up to date, download and install the latest version of Python from this link: https://www.python.org/downloads/.

3. Also, Linux users can install latest version of python by writing in their terminal ```sudo apt install python3.X``` (being X the latest version).

4. To install pip, you only need to ```python -m pip install --upgrade pip``` or ```sudo apt install python3-pip``` depending on your Operating System.

5. After installation is completed, you can install this module by ```pip install -i https://test.pypi.org/simple/ Range-oduranc==0.0.1```

6. To use it, you just need to import it in your python file by importing it ```from range_oduranc import Range```

8. In case you want to execute unit tests files just ```git clone``` this repository, ```cd src/Range_oduranc``` and execute example.py by ```python3 example.py```

## Module Methods Examples

### Constructor
```python
R1 = Range('[2, 7)') # Creates a Range instance that contains the numbers: 2, 3, 4, 5, 6
# NOTE: this R1 will be used for the next examples.
```

### Contains Whole Numbers
```python
result = R1.contains(3, 4, 5) # Check if R1 contains the numbers 3, 4 and 4. Should return True
```

### Get All Points
```python
result = R1.getAllPoints() # Get a list of the whole numbers that exist inside the given range. Should return [2, 3, 4, 5, 6]
```

### Contains Range
```python
result = R1.containsRange('[3, 6]') # Check if R1 contains the given range (in this case [3, 6]). Should return True
```

### Endpoints
```python
result = R1.endPoints() # Get a list of the range endpoints. Should return 2 and 6
```

### Overlaps Range
```python
R2 = Range('[5, 10)')
result = R1.overlapsRange(R2) # Check if R1 and R2 has at least one common element. Should return True
```

### Equals
```python
R3 = Range('(1, 6]')
result = R1.equals(R3) # Check if R1 and R3 has the same elements. Should return True
```
