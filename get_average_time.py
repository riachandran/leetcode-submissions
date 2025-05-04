import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    
    df = activity.pivot_table(index=['machine_id','process_id'],columns='activity_type',values='timestamp').reset_index()
    df['processing_time'] = df['end'] - df['start']
    df = df.groupby('machine_id')['processing_time'].mean().reset_index().round(3)
    return df
