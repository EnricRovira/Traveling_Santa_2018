import pandas as pd

path = [0,1,2,0]

df_path = pd.DataFrame({'CityId':path})
df_path.to_csv("./submissions/minDistances.csv")