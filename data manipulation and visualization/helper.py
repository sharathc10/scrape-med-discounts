import numpy as np

def flatten_df(df,columns_to_flatten,destination_columns):
    '''
    takes a list of columns in a data frame that need to be flattened
    and puts them in destination columns
    e.g. column with list in columns Pharmacies and Phone Numbers
    need to be put in columns Pharmacy and Phone Number
    flatten_df(dataframe, ['Pharmacies','Phone Numbers],['Pharmacy','Phone Number'])
    '''
    #lens_of_lists = df['Pharmacies'].apply(len)
    lens_of_lists = df[columns_to_flatten[0]].apply(len)
    origin_rows = range(df.shape[0])
    destination_rows = np.repeat(origin_rows, lens_of_lists)
    non_list_cols = (
          [idx for idx, col in enumerate(df.columns)
           if col not in columns_to_flatten]
        )
    expanded_df = df.iloc[destination_rows, non_list_cols].copy()
    for idx,col in enumerate(destination_columns):
        expanded_df[col] = (
              [item for items in df[columns_to_flatten[idx]] for item in items]
              )
    expanded_df.reset_index(inplace=True, drop=True)
    return expanded_df