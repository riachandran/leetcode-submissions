import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['max'] = employee.groupby('departmentId')['salary'].transform('max')
    final = employee.merge(department,left_on='departmentId',right_on='id',how='left')
    return final[final['salary']==final['max']].rename(columns={'name_y':'Department','name_x':'Employee','salary':'Salary'})[['Department','Employee','Salary']]
