import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    df = rounds.groupby('interview_id')['score'].sum().reset_index()
    df1 = candidates.merge(df,on='interview_id',how='left')
    return df1[(df1['years_of_exp']>=2)&(df1['score']>15)][['candidate_id']]
