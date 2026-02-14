import pandas as pd
import re


def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    """
    Add a virtual column to a DataFrame based on a mathematical expression.
    
    Args:
        df: Input pandas DataFrame
        role: Mathematical expression (e.g., "column1 + column2")
              Supports operations: +, -, *
        new_column: Name of the new column to be created
        
    Returns:
        New DataFrame with the virtual column added, or empty DataFrame if validation fails
        
    Validation rules:
        - Column names must contain only letters and underscores
        - Only basic operations (+, -, *) are supported
        - All columns referenced in 'role' must exist in the DataFrame
    """
    
    # Validate new column name (only letters and underscores)
    if not re.match(r'^[a-zA-Z_]+$', new_column):
        return pd.DataFrame([])
    
    # Validate role expression (only letters, underscores, spaces, +, -, *)
    if not re.match(r'^[a-zA-Z_\s\+\-\*]+$', role):
        return pd.DataFrame([])
    
    # Extract column names from the expression
    columns_in_role = re.findall(r'[a-zA-Z_]+', role)
    
    # Check if all columns exist in the DataFrame
    if not all(col in df.columns for col in columns_in_role):
        return pd.DataFrame([])
    
    # Create a copy and add the virtual column
    df_copy = df.copy()

    # Evaluate the mathematical expression and add as new column
    try:
        df_copy[new_column] = df_copy.eval(role)
    except Exception:
        # Handle edge cases like "a +", "* b", or other malformed expressions
        return pd.DataFrame([])
    
    return df_copy
