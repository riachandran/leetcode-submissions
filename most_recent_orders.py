import pandas as pd

def most_recent_orders(customers: pd.DataFrame, orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    orders.sort_values(by='order_date',inplace=True)
    orders['rnk'] = orders.groupby('product_id')['order_date'].rank(ascending=False,method='dense')
    final = orders.merge(products,on='product_id',how='left')
    return final[final['rnk']==1][['product_name','product_id','order_id','order_date']].sort_values(by=['product_name','product_id','order_id'],ascending=[1,1,1])
