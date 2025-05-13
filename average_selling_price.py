import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(prices,units_sold,how='left',on=['product_id'])
    df = df[(df['start_date'] <= df['purchase_date']) & (df['end_date'] >= df['purchase_date'])]
    df['total'] = round(df['units']*df['price'],2)
    df = df.groupby('product_id')[['total','units']].sum().reset_index()
    df['average_price'] = round(df['total']/df['units'],2).fillna(0)
    final_df = pd.merge(prices,df,on='product_id',how='left').drop_duplicates(subset='product_id').fillna(0)
    return final_df[['product_id','average_price']]

