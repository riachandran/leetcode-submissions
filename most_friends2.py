import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    friends_count= pd.concat([request_accepted['requester_id'],request_accepted['accepter_id']]).tolist()
    print(friends_count)
    r = mode(friends_count)
    return pd.DataFrame({"id": [r],"num": [friends_count.count(r)]})
