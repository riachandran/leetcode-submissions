import pandas as pd

def find_continuous_ranges(logs: pd.DataFrame) -> pd.DataFrame:
    logs['group'] = logs['log_id'] - logs.index
    return logs.groupby('group').agg(start_id=('log_id','min'), end_id=('log_id','max'))
