import pandas as pd

def sellers_with_no_sales(customer: pd.DataFrame, orders: pd.DataFrame, seller: pd.DataFrame) -> pd.DataFrame:
    df = seller.merge(orders,on='seller_id',how='left')
    return df[['seller_name']][~df['seller_id'].isin(df['seller_id'][df['sale_date'].dt.year == 2020])].sort_values(by='seller_name')
