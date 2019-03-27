import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

train_set = pd.read_csv("./titanic_dataset/train.csv")
