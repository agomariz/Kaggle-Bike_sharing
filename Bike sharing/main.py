import pandas as pd
import Preprocessing as prep

train_data = pd.read_csv('data/train.csv')
preprocessed_data = prep.preprocess(train_data)
print preprocessed_data.describe()