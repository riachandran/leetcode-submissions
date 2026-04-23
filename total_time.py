import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['time'] = employees['out_time'] - employees['in_time']
    return employees.groupby(['event_day','emp_id'])['time'].sum().to_frame('total_time').reset_index().rename(columns={'event_day':'day'})
