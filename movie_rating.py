import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    movie_df = pd.merge(movie_rating, movies, on='movie_id',how='left')
    user_df = pd.merge(movie_df,users,on='user_id',how='left')
    user_df['created_at'] = user_df['created_at'].dt.strftime('%Y-%m')
    movieRating = user_df.groupby('name')['rating'].size().to_frame('ratingCount').sort_values(by='name',ascending=True).sort_values(by='ratingCount',kind='stable',ascending=False).reset_index()
    avgRating = user_df[user_df['created_at']=='2020-02'].groupby('title')['rating'].mean().to_frame('avg_rating').sort_values(by='title',ascending=True).sort_values(by='avg_rating',kind='stable',ascending=False).reset_index()
    return pd.DataFrame({'results':[movieRating['name'][0],avgRating['title'][0]]})
