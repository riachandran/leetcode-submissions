import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(customers,orders,on='customer_id',how='right')
    df = df.groupby('customer_id').agg(
        A = ('product_name',lambda x: (x=='A').any()),
        B = ('product_name',lambda x: (x=='B').any()),
        C = ('product_name',lambda x: (x=='C').any())
    ).reset_index()
    final = pd.merge(customers,df,on='customer_id',how='left').dropna()
    return final[['customer_id','customer_name']][final['A'] & final['B'] & ~final['C']]
    
