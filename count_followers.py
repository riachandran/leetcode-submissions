import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    df = followers.groupby('user_id')['follower_id'].size().to_frame('followers_count').reset_index()
    return df
