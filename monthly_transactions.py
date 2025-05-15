import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['month'] = transactions['trans_date'].dt.strftime('%Y-%m')
    transactions['appr_count'] = transactions.apply(lambda row: 1 if row['state'] == 'approved' else 0,axis=1)
    transactions['appr_amt'] = transactions.apply(lambda row: row['amount'] if row['state'] == 'approved' else 0,axis=1)
    df = transactions.groupby(['month','country'], dropna=False).agg(trans_count=('state','count'),approved_count=('appr_count','sum'),trans_total_amount=('amount','sum'),approved_total_amount=('appr_amt','sum')).reset_index()
    return df
