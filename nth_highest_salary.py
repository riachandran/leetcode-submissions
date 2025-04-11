import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted_salaries = employee['salary'].sort_values(ascending=False).drop_duplicates()
    if N > len(sorted_salaries) or N <= 0:
        return pd.DataFrame({'getNthHighestSalary('+str(N)+')': [None]})
    else:
        result = sorted_salaries.iloc[N-1]
    return pd.DataFrame({'getNthHighestSalary('+str(N)+')': [result]})
