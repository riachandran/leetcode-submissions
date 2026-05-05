import pandas as pd

def find_safe_countries(person: pd.DataFrame, country: pd.DataFrame, calls: pd.DataFrame) -> pd.DataFrame:
    person['country_code'] = person['phone_number'].str[:3]
    df1 = pd.merge(person,country,on='country_code',how='left')
    df2 = pd.merge(calls,df1,left_on='caller_id',right_on='id',how='left')
    df3 = pd.merge(calls,df1,left_on='callee_id',right_on='id',how='left')
    df4 = pd.concat([df2[['name_y','duration']],df3[['name_y','duration']]])
    final = df4.groupby('name_y')['duration'].mean().reset_index().rename(columns={'name_y':'country'})
    return final[['country']][final['duration']>df4['duration'].mean()]
