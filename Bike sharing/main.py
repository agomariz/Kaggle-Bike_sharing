import pandas as pd
import Preprocessing as prep

train_data = pd.read_csv('data/train.csv')

print prep.create_dummies(train_data,'season').describe()