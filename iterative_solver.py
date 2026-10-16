import pandas as pd
import numpy as np
from tabulate import tabulate

def iterative_solver_table(A, b=None, x0=None, iterations=5, method='gauss-seidel', grid_style='grid'):
    """
    Solves Ax = b iteratively and outputs a grid table with horizontal lines between rows.
    
    Column Order:
    Iteration (k) | x1, x2... | Rel Err x1 (%), Rel Err x2 (%)... | Abs Err x1, Abs Err x2...
    """
    A = np.array(A, dtype=float)
    n = A.shape[0]
    
    # Defaults if b or x0 are omitted
    b = np.zeros(n, dtype=float) if b is None else np.array(b, dtype=float)
    x = np.zeros(n, dtype=float) if x0 is None else np.array(x0, dtype=float)

    var_names = [f'x{i+1}' for i in range(n)]
    records = []
    
    # Iteration k = 0 (Initial Guess)
    row_0 = {'Iteration (k)': 0}
    for name in var_names:
        row_0[name] = round(x[int(name[1:]) - 1], 4)
        row_0[f'Rel Err {name} (%)'] = "-"
        row_0[f'Abs Err {name}'] = "-"
    records.append(row_0)

    # Iterations k = 1 to N
    for k in range(1, iterations + 1):
        x_old = x.copy()
        
        if method.lower() == 'gauss-seidel':
            for i in range(n):
                s = sum(A[i][j] * x[j] for j in range(n) if j != i)
                x[i] = (b[i] - s) / A[i][i]
                
        elif method.lower() == 'jacobi':
            x_next = np.zeros(n)
            for i in range(n):
                s = sum(A[i][j] * x_old[j] for j in range(n) if j != i)
                x_next[i] = (b[i] - s) / A[i][i]
            x = x_next

        row = {'Iteration (k)': k}
        
        # 1. Variable values (x1, x2...)
        for i, name in enumerate(var_names):
            row[name] = round(x[i], 4)
            
        # 2. Relative Errors (%)
        for i, name in enumerate(var_names):
            abs_err = abs(x[i] - x_old[i])
            if x[i] != 0:
                rel_err = abs(abs_err / x[i]) * 100
                row[f'Rel Err {name} (%)'] = round(rel_err, 2)
            else:
                row[f'Rel Err {name} (%)'] = "-"
                
        # 3. Absolute Errors
        for i, name in enumerate(var_names):
            abs_err = abs(x[i] - x_old[i])
            row[f'Abs Err {name}'] = round(abs_err, 4)
                    
        records.append(row)

    df = pd.DataFrame(records)
    
    # Reorder columns explicitly: Iteration -> Values -> Rel Errors -> Abs Errors
    col_order = ['Iteration (k)']
    col_order += [f'x{i+1}' for i in range(n)]
    col_order += [f'Rel Err x{i+1} (%)' for i in range(n)]
    col_order += [f'Abs Err x{i+1}' for i in range(n)]
    
    df = df[col_order]
    
    # Render table with lines between every row
    return tabulate(df, headers='keys', tablefmt=grid_style, showindex=False)
# Matrix A only (2 variables x1, x2; b vector omitted)
A_2D = [
    [2, 1],
    [1, 2]
]
b = [2, -5]
# Set a non-zero initial guess to observe convergence to 0
x0_2D = [1, -1] 

table_output = iterative_solver_table(A_2D,b=b, x0=x0_2D, iterations=3, method='gauss-seidel')
print(table_output)