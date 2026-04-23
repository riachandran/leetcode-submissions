import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    logins = logins[logins['time_stamp'].dt.year==2020]
    return logins.groupby('user_id')['time_stamp'].max().to_frame('last_stamp').reset_index()
