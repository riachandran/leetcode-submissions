import pandas as pd

def apples_oranges(sales: pd.DataFrame) -> pd.DataFrame:
    sales = sales.pivot_table(index='sale_date',columns='fruit',values='sold_num').reset_index()
    sales['diff'] = sales['apples'] - sales['oranges']
    return sales[['sale_date','diff']]
