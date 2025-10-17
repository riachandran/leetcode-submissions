def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    daily = customer.groupby('visited_on')['amount'].sum().reset_index()
    daily['amount'] = daily['amount'].rolling(window=7).sum()
    daily['average_amount'] = (daily['amount']/7).round(2)
    return daily.dropna().reset_index(drop=True)
