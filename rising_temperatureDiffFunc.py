import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by='recordDate',inplace=True)
    weather['previousTemp'] = weather['temperature'].shift(1)
    return weather[['id']][(weather['temperature'].diff() > 0) & (weather['recordDate'].diff().dt.days == 1)]
