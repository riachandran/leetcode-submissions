import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    df = confirmations.action.eq('confirmed').groupby(confirmations['user_id'])
    df = df.transform('sum')/df.transform('size')
    confirmations['confirmation_rate'] = df
    df = confirmations.groupby(['user_id']).mean('confirmation_rate')
    final_df = pd.merge(signups,df,on='user_id',how='left').sort_values(by='time_stamp',ascending=False)
    final_df['confirmation_rate'] = round(final_df['confirmation_rate'],2).fillna(0)
    return final_df[['user_id','confirmation_rate']]
