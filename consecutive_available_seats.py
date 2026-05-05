import pandas as pd

def consecutive_available_seats(cinema: pd.DataFrame) -> pd.DataFrame:
    cinema['before'] = cinema['free'].shift(-1)
    cinema['after'] = cinema['free'].shift(1)
    return cinema[['seat_id']][((cinema['before']==1)&(cinema['free']==1))|((cinema['after']==1)&(cinema['free']==1))].sort_values(by='seat_id')
