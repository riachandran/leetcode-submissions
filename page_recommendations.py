import pandas as pd

def page_recommendations(friendship: pd.DataFrame, likes: pd.DataFrame) -> pd.DataFrame:
    df = pd.concat([friendship[friendship['user1_id']==1].user2_id,friendship[friendship['user2_id']==1].user1_id]).to_frame('ids')
    avoid = likes[['page_id']][likes['user_id']==1]
    return likes[['page_id']][(likes['user_id'].isin(df['ids']))&(~likes['page_id'].isin(avoid['page_id']))].drop_duplicates().rename(columns={'page_id':'recommended_page'})
