import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df1 = orders.merge(company,on='com_id',how='left')
    df1 = df1[df1['name']=='RED']
    final = pd.merge(sales_person,df1,on='sales_id',how='left')
    return final[['name_x']][final['name_y'].isna()].rename(columns={'name_x':'name'})
