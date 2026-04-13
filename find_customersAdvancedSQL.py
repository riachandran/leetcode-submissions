import pandas as pd

def find_customers(customers: pd.DataFrame) -> pd.DataFrame:
    return customers[['customer_id']][(customers['year']==2021)&(customers['revenue']>0)]
