import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.groupby('player_id')['event_date'].min().to_frame('first_login').reset_index()
