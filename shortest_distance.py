import pandas as pd

def shortest_distance(point: pd.DataFrame) -> pd.DataFrame:
    point.sort_values(by='x',inplace=True)
    point['dist'] = point['x'].shift(-1).dropna()
    point['shortest'] = abs(point['x']-point['dist'])
    return pd.DataFrame({'shortest':[point['shortest'].min()]})
