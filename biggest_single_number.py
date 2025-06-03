import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df = my_numbers['num'].value_counts().reset_index()
    return df[['num']][df['count']==1].max().to_frame('num')
