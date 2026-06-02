import pandas as pd

def team_size(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby('team_id')['team_id'].value_counts().to_frame('team_size').reset_index()
    return employee.merge(df,on='team_id',how='left')[['employee_id','team_size']]
