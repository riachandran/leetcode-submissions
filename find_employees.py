import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    df = pd.concat([employees,salaries])
    df = df.groupby('employee_id')['employee_id'].count().to_frame('cnt').reset_index()
    return df[['employee_id']][df['cnt']!=2]
