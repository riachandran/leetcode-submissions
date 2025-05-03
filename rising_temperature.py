import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by='recordDate',inplace=True)
    weather['prev_temp'] = weather['temperature'].shift(1)
    weather['prev_recordDate'] = weather['recordDate'].shift(1)

    weather['prev_recordDate'] = pd.to_datetime(weather['prev_recordDate'])
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])

    result = weather[(weather['recordDate'] - weather['prev_recordDate'] == pd.Timedelta(days=1)) & (weather['temperature'] > weather['prev_temp'])]
    return result[['id']]
