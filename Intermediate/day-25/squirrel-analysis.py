import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).parent

df = pd.read_csv(BASE_DIR / '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# print(df['Primary Fur Color'])
gray = df[df['Primary Fur Color'] == "Gray"]
black = df[df['Primary Fur Color'] == "Black"]
cinnamon = df[df['Primary Fur Color'] == "Cinnamon"]

data_dict = {
    'color' : ['gray', 'black', 'cinnamon'],
    'count' : [len(gray), len(black), len(cinnamon)]
}

fur_counts_df = pd.DataFrame(data_dict)
fur_counts_df.to_csv(BASE_DIR / "squirrel_counts.csv")