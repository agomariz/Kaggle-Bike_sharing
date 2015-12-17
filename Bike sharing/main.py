import pandas as pd
import Preprocessing as prep

train_data = pd.read_csv('data/train.csv')
train_data = prep.process_date_column(train_data,'datetime')
train_data = prep.get_parts_of_days(train_data, 'hour')

print train_data.describe()

print prep.create_dummies(train_data, ['year','month','day','hour','season', 'holiday', 'workingday', 'weather', 'part_of_day']).describe()