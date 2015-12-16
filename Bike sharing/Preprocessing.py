import pandas as pd

def _create_dummies(df,column):
    '''
    Exchange a categorical column by dummy columns in a Pandas dataframe
    :param df:
    :param column:
    :return:
    '''
    dummy_df = pd.get_dummies(df[column], prefix='Season')
    df = pd.concat([df,dummy_df],axis=1)
    return df.drop(column, 1)