import pandas as pd

def highest_grade(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values(by=['student_id','grade','course_id'],ascending=[1,0,1]).groupby('student_id').head(1)
