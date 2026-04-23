import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders.groupby('customer_number')['order_number'].count().reset_index().sort_values(by='order_number').tail(1)[['customer_number']]
