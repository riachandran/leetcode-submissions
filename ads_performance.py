import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    ads['clicked'] = (ads['action']=='Clicked').astype(int)
    ads['viewed'] = (ads['action']=='Viewed').astype(int)
    df = ads.groupby('ad_id').agg(tot_ctr = ('clicked','sum'), tot_view = ('viewed','sum')).reset_index()
    print(df)
    df['ctr'] = (df['tot_ctr']*100/(df['tot_ctr']+df['tot_view'])).round(2).fillna(0)
    return df[['ad_id','ctr']].sort_values(by=['ctr','ad_id'],ascending=[0,1])
