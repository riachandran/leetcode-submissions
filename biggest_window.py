import pandas as pd

def biggest_window(user_visits: pd.DataFrame) -> pd.DataFrame:
    user_visits.sort_values(by=['user_id','visit_date'],ascending=[1,1],inplace=True)
    user_visits['windate'] = user_visits.groupby('user_id')['visit_date'].shift(-1).fillna('2021-1-1')
    user_visits['biggest_window'] = (user_visits['windate'] - user_visits['visit_date']).dt.days
    return user_visits.groupby('user_id')['biggest_window'].max().reset_index()
