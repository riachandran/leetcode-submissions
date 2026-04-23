import pandas as pd

def number_of_calls(calls: pd.DataFrame) -> pd.DataFrame:
    calls[['person1','person2']] = np.sort(calls[['from_id','to_id']],axis=1)
    return calls.groupby(['person1','person2']).agg(call_count=('duration','count'),total_duration=('duration','sum')).reset_index()
