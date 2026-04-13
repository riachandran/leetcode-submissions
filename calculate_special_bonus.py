import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda x: 0 if (x['employee_id']%2 == 0) or (x['name'].startswith('M')) else x['salary'], axis = 1)
    return employees[['employee_id','bonus']].sort_values(by='employee_id')
