import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    end_date = pd.to_datetime('2019-07-27')
    start_date = end_date - pd.DateOffset(days=29)

    df = activity[activity['activity_date'].between(start_date,end_date)]
    df = df.groupby('activity_date')['user_id'].nunique().reset_index(name='active_users').rename(columns={'activity_date':'day'})
    return df
