import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    unique_users = users['user_id'].nunique()
    df = register.groupby('contest_id')['user_id'].nunique().to_frame('count').reset_index()
    df['percentage'] = round((df['count']/unique_users) * 100,2).fillna(0)
    return df[['contest_id','percentage']].sort_values(by=['contest_id']).sort_values(by=['percentage'],kind='stable',ascending=False)
