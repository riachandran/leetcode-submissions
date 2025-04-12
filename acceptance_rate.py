import pandas as pd

def acceptance_rate(friend_request: pd.DataFrame, request_accepted: pd.DataFrame) -> pd.DataFrame:
    accepted_requests = len(request_accepted.groupby(['requester_id','accepter_id']))
    friend_requests = len(friend_request.groupby(['sender_id','send_to_id']))
    if len(friend_request) <= 0: return pd.DataFrame({'accept_rate':[0.00000]})
    else: 
        result = round(accepted_requests/friend_requests,2)
        return pd.DataFrame({'accept_rate':[float(f"{result:.5f}")]})
