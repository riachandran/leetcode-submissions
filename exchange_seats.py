import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    def swap(x):
        if x % 2 == 0:
            return x - 1
        elif x < seat['id'].max():
            return x + 1
        else:
            return x

    seat['new_id'] = seat['id'].apply(swap)
    return seat[['new_id','student']].sort_values(by='new_id').rename(columns={'new_id':'id'})
