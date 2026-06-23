import pandas as pd

def find_subtasks(tasks: pd.DataFrame, executed: pd.DataFrame) -> pd.DataFrame:
    tasks['subtask_id'] = tasks['subtasks_count'].apply(lambda x: list(range(1,x+1)))
    tasks = tasks.explode('subtask_id')
    tasks = tasks.merge(executed, on=['task_id','subtask_id'],how='left',indicator=True)
    return tasks[tasks['_merge']=='left_only'][['task_id','subtask_id']]
