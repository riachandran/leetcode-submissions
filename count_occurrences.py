import pandas as pd

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    result = {'bull':0,'bear':0}
    for f in files.itertuples():
        if re.search(r'\sbull\s',f.content): result['bull'] += 1
        if re.search(r'\sbear\s',f.content): result['bear'] += 1

    return pd.DataFrame(list(result.items()),columns=['word','count'])
