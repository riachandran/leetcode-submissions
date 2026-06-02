import pandas as pd

def leetflex_banned_accnts(log_info: pd.DataFrame) -> pd.DataFrame:
    df = log_info.merge(log_info,on='account_id',suffixes=['_a','_b'])
    df = df[df['ip_address_a']!=df['ip_address_b']]
    df = df[(df['login_a']<=df['logout_b'])&(df['login_b']<=df['logout_a'])]
    return pd.DataFrame({'account_id':df['account_id'].unique()})
