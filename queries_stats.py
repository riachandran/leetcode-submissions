import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries['ratio'] = queries['rating']/queries['position'] +1e-6
    queries['rating_check'] = queries.apply(lambda row: 1 if row['rating']<3 else 0, axis=1)
    df = queries.groupby("query_name").agg(quality=('ratio','mean'),rating_count=('rating_check','sum'),rating_total=('rating_check','count')).reset_index()
    df['poor_query_percentage'] = round(df['rating_count']*100/df['rating_total'],2)
    df['quality'] = round(df['quality'],2)
    return df[['query_name','quality','poor_query_percentage']]
