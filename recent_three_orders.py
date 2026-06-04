import pandas as pd

def recent_three_orders(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.merge(customers,on='customer_id',how='left').rename(columns={'name':'customer_name'})
    df['rnk'] = df.groupby('customer_id')['order_date'].rank(ascending=False,method='dense')
    return df[df['rnk']<=3][['customer_name','customer_id','order_id','order_date']].sort_values(by=['customer_name','customer_id','order_date'],ascending=[1,1,0])
