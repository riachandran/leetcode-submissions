import pandas as pd

def team_scores(teams: pd.DataFrame, matches: pd.DataFrame) -> pd.DataFrame:
    hosts = matches[['host_team','host_goals','guest_goals']].rename(columns={'host_team':'team_id','host_goals':'goals_for','guest_goals':'goals_against'})
    guests = matches[['guest_team','host_goals','guest_goals']].rename(columns={'guest_team':'team_id','guest_goals':'goals_for','host_goals':'goals_against'})
    games = pd.concat([hosts,guests])
    conditions = [(games['goals_for']>games['goals_against']),(games['goals_for']==games['goals_against'])]
    choices = [3,1]
    games['wins'] = np.select(conditions,choices,default=0)
    games = games.groupby('team_id')['wins'].sum().to_frame('num_points').reset_index()
    result = pd.merge(teams,games,on='team_id',how='left').fillna(0)
    return result.sort_values(by=['num_points','team_id'],ascending=[0,1])
