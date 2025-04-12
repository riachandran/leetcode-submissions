import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    join_emp = pd.merge(employee,department, left_on='departmentId', right_on='id').sort_values(by='salary',ascending=False).rename(columns={'name_y':'Department','name_x':'Employee','salary':'Salary'})[['Department','Employee','Salary']]
    join_emp['rank'] = join_emp.groupby('Department')['Salary'].rank(method='dense',ascending=False)
    return join_emp[['Department','Employee','Salary']][join_emp['rank']<=3]
