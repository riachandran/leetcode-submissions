import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.groupby('reports_to',as_index=False).agg(reports_count=('employee_id','size'),average_age=('age',lambda x: int(x.mean()+0.5)))
    return df.merge(employees, left_on = "reports_to", right_on = "employee_id")[["employee_id","name","reports_count","average_age"]].sort_values(by=["employee_id"])
