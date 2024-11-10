import pandas as pd

import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

print(f"\n\n\n {x}")