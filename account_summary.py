import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = transactions.groupby('account')['amount'].sum().to_frame('balance').reset_index()
    result = users.merge(df,on='account',how='right')[['name','balance']]
    return result[result['balance']>10000]
