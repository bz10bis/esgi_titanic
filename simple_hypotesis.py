import pandas as pd
import numpy as np

train_set = pd.read_csv("./titanic_dataset/train.csv")

simple_hypotesis = train_set.copy()

simple_hypotesis["Hypotesis"] = 0
simple_hypotesis.loc[simple_hypotesis.Sex == "female", "Hypotesis"] = 1
simple_hypotesis["Result"] = 0
simple_hypotesis.loc[simple_hypotesis.Survived == simple_hypotesis["Hypotesis"], "Result"] = 1
print(simple_hypotesis["Result"].value_counts(normalize=True))
