import pandas as pd
import numpy as np

def _create_dummy(df,column):
    '''
    Exchange a categorical column by dummy columns in a Pandas dataframe
    :param df:
    :param column:
    :return:
    '''
    dummy_df = pd.get_dummies(df[column], prefix=column)
    df = pd.concat([df,dummy_df],axis=1)
    return df.drop(column, 1)

def create_dummies(df, columns):
    for c in columns:
        df = _create_dummy(df,c)
    return df

def process_date_column(df,column):
    df['year'] = pd.to_datetime(df[column]).dt.year
    df['month'] = pd.to_datetime(df[column]).dt.month
    df['day'] = pd.to_datetime(df[column]).dt.day
    df['weekday'] = pd.to_datetime(df[column]).dt.weekday
    df['hour'] = pd.to_datetime(df[column]).dt.hour

    return df.drop(column, 1)

def get_parts_of_days(df, column):
    def _get_part_of_day(h):
        res = 'night'
        if 6<=h<13: res = 'morning'
        elif 13<=h<19: res = 'afternoon'
        elif 19<=h<23: res = 'evening'
        return res

    df['part_of_day'] = df[column].map(lambda h:_get_part_of_day(h))
    return df

def preprocess(df):

    df = process_date_column(df,'datetime')
    df = get_parts_of_days(df, 'hour')

    # Uncomment if we want to remove any column
    # df = df.drop(['month', 'day'], axis=1)

    df = create_dummies(df, ['year','month','day','weekday','hour','season', 'holiday',
                             'workingday', 'weather', 'part_of_day'])
    return df