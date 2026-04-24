import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = person.groupby('email')['email'].count().to_frame('cnt').reset_index().rename(columns={'email':'Email'})
    return df[['Email']][df['cnt']>1]
