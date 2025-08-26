import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue.sort_values(by='turn',inplace=True)
    queue['totalw'] = queue['weight'].cumsum()
    return queue.loc[queue.totalw <= 1000, ['person_name']].tail(1)
