import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby('employee_id')['department_id'].size().to_frame('count').reset_index()
    df = df[df['count'] == 1]
    return employee[['employee_id','department_id']][(employee['primary_flag'] == 'Y') | (employee['employee_id'].isin(df['employee_id']))]
