import pandas as pd

idx= [1,2,3,4,5]
s=pd.DataFrame(['A','B','C','D','E'],index=idx)
print(s)
s['new'] = s.index + 1
s = s['new']
print(s)