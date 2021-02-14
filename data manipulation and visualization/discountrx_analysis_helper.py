def min_within_group(df):
    minPrice_stores=df.loc[df.groupby('Drug name')['Price'].idxmin()]
    minPrice_counts = minPrice_stores['Store Type'].value_counts()
    return minPrice_counts

def max_within_group(df):
    maxPrice_stores=df.loc[df.groupby('Drug name')['Price'].idxmax()]
    maxPrice_counts = maxPrice_stores['Store Type'].value_counts()
    return maxPrice_counts