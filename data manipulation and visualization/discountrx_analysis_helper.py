def min_within_group(df):
    minPrice_stores=df.loc[df.groupby('Drug name')['Price'].idxmin()]
    minPrice_counts = minPrice_stores['Store Type'].value_counts()
    return minPrice_counts

def max_within_group(df):
    maxPrice_stores=df.loc[df.groupby('Drug name')['Price'].idxmax()]
    maxPrice_counts = maxPrice_stores['Store Type'].value_counts()
    return maxPrice_counts

def store_type_color_palette(dat):
    return ["#a6cee3" if x=='Department Store' else 
                          ('#1f78b4' if x=="Grocery Chain" else 
                           ("#b2df8a" if x=="Local Pharmacy" else 
                            ("#33a02c" if x== "Pharmacy Chain" else "#fb9a99"))) for x in dat]