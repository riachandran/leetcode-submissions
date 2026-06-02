import pandas as pd

def grand_slam_titles(players: pd.DataFrame, championships: pd.DataFrame) -> pd.DataFrame:
    df1 = championships.groupby('Wimbledon')['Wimbledon'].value_counts().to_frame('grand_slams_count').reset_index().rename(columns={'Wimbledon':'player_id'})
    df2 = championships.groupby('Fr_open')['Fr_open'].value_counts().to_frame('grand_slams_count').reset_index().rename(columns={'Fr_open':'player_id'})
    df3 = championships.groupby('US_open')['US_open'].value_counts().to_frame('grand_slams_count').reset_index().rename(columns={'US_open':'player_id'})
    df4 = championships.groupby('Au_open')['Au_open'].value_counts().to_frame('grand_slams_count').reset_index().rename(columns={'Au_open':'player_id'})
    df = pd.concat([df1,df2,df3,df4]).groupby('player_id')['grand_slams_count'].sum().reset_index()
    return df.merge(players,on='player_id',how='left')
