import pandas as pd

def most_frequently_products(customers: pd.DataFrame, orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    orders = orders.merge(customers,on='customer_id',how='left')
    orders = orders.merge(products,on='product_id',how='left')
    df = orders.groupby(['customer_id','product_id'])['product_name'].value_counts().to_frame('count').reset_index().sort_values(by=['customer_id','count'],ascending=[1,0])
    df = df[df['count']==df.groupby('customer_id')['count'].transform('max')]
    return df[['customer_id','product_id','product_name']]
