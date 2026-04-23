import pandas as pd

def warehouse_manager(warehouse: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    products['vol'] = products['Width']*products['Length']*products['Height']
    warehouse = warehouse.merge(products[['product_id','vol']],on='product_id',how='left').rename(columns={'name':'warehouse_name'})
    warehouse['vol'] *= warehouse['units']
    return warehouse.groupby('warehouse_name')['vol'].sum().to_frame('volume').reset_index()
