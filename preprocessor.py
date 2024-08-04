import pandas as pd

def preprocess(df, region_df):


    # Filtering the dataframe for 'Summer' season
    df = df[df['Season'] == 'Summer']

    # Checking the sizes of dataframes before merging
    print("Original dataframe size:", df.shape)
    print("Region dataframe size:", region_df.shape)

    # Merging dataframes on 'NOC' column
    df = df.merge(region_df, on='NOC', how='left')

    # Dropping duplicates if any
    df.drop_duplicates(inplace=True)

    # Checking the size of the dataframe after merging
    print("Merged dataframe size:", df.shape)

    # Creating dummy variables for 'Medal' column
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df
