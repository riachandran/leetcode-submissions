import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = sales.groupby('product_id')[['year','quantity','price']].agg(year=('year','min')).reset_index()
    final_df = pd.merge(sales,df,how='inner',on=['product_id','year']).rename(columns={'year':'first_year'})
    return final_df[['product_id','first_year','quantity','price']]
