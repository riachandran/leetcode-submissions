import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df = students.merge(subjects,how='cross')
    exam_df = examinations.groupby(['student_id','subject_name']).value_counts().to_frame('attended_exams').reset_index()
    final_df = pd.merge(df,exam_df,on=['student_id','subject_name'],how='left').sort_values(by=['student_id','subject_name'])
    final_df['attended_exams'] = final_df['attended_exams'].fillna(0)
    return final_df
