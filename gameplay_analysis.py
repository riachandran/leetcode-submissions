import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.groupby('player_id')['event_date'].min().reset_index()
    merge = activity.merge(df,on=['player_id','event_date'])
    df['event_date'] = df['event_date'] + pd.Timedelta(days=1)
    merge2 = activity.merge(df,on=['player_id','event_date'])
    return pd.DataFrame({'fraction':[round(len(merge2['player_id'])/len(merge['player_id']),2)]})
