import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    store = store[store['amount']>500]
    return pd.DataFrame({'rich_count':[store['customer_id'].nunique()]})
