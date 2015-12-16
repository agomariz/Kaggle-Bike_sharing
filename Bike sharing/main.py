import pandas as pd
import Preprocessing as prep

train_data = pd.read_csv('data/train.csv')
train_data = prep.process_date_column(train_data,'datetime')

print train_data.describe()

print prep.create_dummies(train_data, ['year','month','day','hour','season', 'holiday', 'workingday', 'weather']).describe()