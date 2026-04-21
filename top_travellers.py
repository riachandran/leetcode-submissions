import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    df = users.merge(rides,left_on='id',right_on='user_id',how='left').fillna(0)
    return df.groupby(['name','user_id'])['distance'].sum().to_frame('travelled_distance').reset_index().sort_values(by=['travelled_distance','name'],ascending=[0,1])[['name','travelled_distance']]
