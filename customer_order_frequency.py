import pandas as pd

def customer_order_frequency(customers: pd.DataFrame, product: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df1 = pd.merge(orders,customers,on='customer_id',how='left')
    df2 = pd.merge(df1,product,on='product_id',how='left')
    df2 = df2[(df2['order_date'].dt.year==2020)&((df2['order_date'].dt.month==6) | (df2['order_date'].dt.month==7))]
    df2['total'] = df2.apply(lambda x: x['price']*x['quantity'],axis=1)
    final = df2.groupby(['customer_id','name',df2['order_date'].dt.month])['total'].sum().reset_index()
    final = final[final['total'] >= 100]
    final = final.groupby(['customer_id','name'])['order_date'].size().reset_index()
    return final[['customer_id','name']][final['order_date']==2]
