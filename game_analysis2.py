import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.groupby('player_id')['event_date'].min().reset_index()
    return activity.merge(df,on=['player_id','event_date'],how='right')[['player_id','device_id']]
