import pandas as pd

def find_quiet_students(student: pd.DataFrame, exam: pd.DataFrame) -> pd.DataFrame:
    scores = exam.groupby('exam_id').agg(highest=('score','max'),lowest=('score','min')).reset_index()
    exam = exam.merge(scores,on='exam_id',how='left')
    quiet = exam[(exam['score']!=exam['highest'])&(exam['score']!=exam['lowest'])]
    exam['quiet_count'] = exam.apply(lambda x: 1 if x['score']==x['highest'] or x['score']==x['lowest'] else 0, axis=1)
    df2 = exam.groupby('student_id')['quiet_count'].sum().reset_index()
    final = df2[df2['quiet_count']==0][['student_id']].sort_values(by='student_id')
    final = final.merge(student,on='student_id',how='left').sort_values(by='student_id')
    return final
