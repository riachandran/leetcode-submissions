import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({'immediate_percentage':[round((delivery.loc[delivery['order_date']==delivery['customer_pref_delivery_date'],'delivery_id'].count()*100)/delivery['delivery_id'].count(),2)]})
