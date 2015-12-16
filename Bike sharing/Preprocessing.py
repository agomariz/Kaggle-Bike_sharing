import pandas as pd

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
    df['hour'] = pd.to_datetime(df[column]).dt.hour

    return df.drop(column, 1)

