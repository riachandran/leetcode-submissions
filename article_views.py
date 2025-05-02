import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    ids = views[['author_id']][views['author_id']==views['viewer_id']].sort_values(by='author_id').drop_duplicates()
    return pd.DataFrame({'id':ids['author_id']})
