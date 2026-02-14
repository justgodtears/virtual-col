# Recruitment Task - Virtual Columns in Pandas DataFrame

## Task Description

Implement a function that adds a virtual (calculated) column to a pandas DataFrame based on a mathematical expression.

## Solution

The `add_virtual_column` function:
- Takes a DataFrame and a mathematical expression
- Validates column names and expressions
- Returns a new DataFrame with the calculated column

### Supported Operations
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)

### Validation Rules
- Column names must contain only letters and underscores
- All columns referenced in the expression must exist
- Invalid input returns an empty DataFrame

## Usage
```python
import pandas as pd
from solution import add_virtual_column

df = pd.DataFrame({
    'quantity': [10, 3],
    'price': [10, 1]
})

result = add_virtual_column(df, "quantity * price", "total")
print(result)
```

Output:
```
   quantity  price  total
0        10     10    100
1         3      1      3
```

## Running Tests
```bash
pytest test_solution.py
```

## Author
justgodtears
