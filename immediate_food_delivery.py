import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery = delivery.sort_values(by='order_date').drop_duplicates(subset=['customer_id'])
    count = (delivery['order_date'] == delivery['customer_pref_delivery_date']).sum()
    return pd.DataFrame({'immediate_percentage':[round(count*100/delivery.shape[0],2)]})
