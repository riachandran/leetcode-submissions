import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(products,orders,how='left',on='product_id')
    df['order_date'] = df['order_date'].dt.strftime('%Y-%m')
    df = df[df['order_date']=='2020-02'].groupby('product_name')['unit'].sum().reset_index()
    return df[df['unit']>=100]
