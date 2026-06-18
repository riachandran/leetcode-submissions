import pandas as pd

def find_reporting_people(employees: pd.DataFrame) -> pd.DataFrame:
    direct_reportees = employees[(employees['manager_id']==1)&(employees['employee_id']!=1)][['employee_id']]
    indirect_reportees = employees[employees['manager_id'].isin(direct_reportees['employee_id'])][['employee_id']]
    indirect_second_reportees = employees[employees['manager_id'].isin(indirect_reportees['employee_id'])][['employee_id']]
    return pd.concat([direct_reportees,indirect_reportees,indirect_second_reportees])
