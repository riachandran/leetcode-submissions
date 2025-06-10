import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = customer.groupby('customer_id')['product_key'].nunique().reset_index()
    n_prod = product['product_key'].count()
    return df[['customer_id']][df['product_key']==n_prod]
