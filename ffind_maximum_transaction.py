import pandas as pd

def find_maximum_transaction(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['date'] = transactions['day'].dt.date
    transactions['rnk'] = transactions.groupby('date')['amount'].rank(ascending=False,method='dense')
    return transactions[transactions['rnk']==1][['transaction_id']].sort_values(by='transaction_id')
