import pandas as pd

def eval_expression(variables: pd.DataFrame, expressions: pd.DataFrame) -> pd.DataFrame:
    variable_dict = dict(zip(variables['name'],variables['value']))

    def evaluate_row(row):
        value1 = variable_dict.get(row['left_operand'])
        value2 = variable_dict.get(row['right_operand'])

        if value1 is None or value2 is None:
            return None
        
        op = row['operator'].replace('=','==')

        return str(eval(f"{value1}{op}{value2}")).lower()


    expressions['value'] = expressions.apply(lambda row: evaluate_row(row),axis=1)

    return expressions
