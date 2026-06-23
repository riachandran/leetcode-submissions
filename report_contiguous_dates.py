import pandas as pd

def report_contiguous_dates(failed: pd.DataFrame, succeeded: pd.DataFrame) -> pd.DataFrame:
    failed['period_state'] = 'failed'
    succeeded['period_state'] = 'succeeded'
    failed = failed.rename(columns={'fail_date':'date'})
    succeeded = succeeded.rename(columns={'success_date':'date'})
    df = pd.concat([failed,succeeded]).sort_values(by='date')
    df = df[df['date'].between('2019-01-01','2019-12-31')]
    df['period'] = (df['period_state']!=df['period_state'].shift()).cumsum()
    df = df.groupby(['period','period_state']).agg(start_date=('date','min'),end_date=('date','max')).reset_index()
    return df[['period_state','start_date','end_date']].sort_values(by='start_date')
