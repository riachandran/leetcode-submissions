import pandas as pd

def project_employees(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(project,on='employee_id',how='left')
    df['rank'] = df.groupby('project_id')['experience_years'].rank(ascending=False,method='dense')
    return df[df['rank']==1][['project_id','employee_id']]
