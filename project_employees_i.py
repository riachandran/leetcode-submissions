import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(project,employee,on='employee_id',how='left')
    df = df.groupby('project_id')['experience_years'].mean().to_frame('average_years').reset_index('project_id')
    df['average_years'] = round(df['average_years'],2)
    return df
