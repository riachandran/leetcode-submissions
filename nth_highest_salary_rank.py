import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee['rnk'] = employee['salary'].rank(method='dense',ascending=False)
    result = employee[employee['rnk']==N]['salary'].drop_duplicates()
    if result.empty:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    return pd.DataFrame({f'getNthHighestSalary({N})': result})
