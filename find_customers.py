import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers_not_ordered = customers[~customers['id'].isin(orders['customerId'])]['name']
    return pd.DataFrame({'Customers': [customer for customer in customers_not_ordered]})
